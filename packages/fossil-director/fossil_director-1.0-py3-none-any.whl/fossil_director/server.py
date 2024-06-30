"""
Asynchronous HTTP server for dispatching fossil repositories 
to configurable virtual hosts
"""
import os.path
import asyncio
import re
import sys


class Redirect(Exception):
    def __init__(self, url):
        self.url = url


class BadHost(Exception):
    pass


class HttpProtocol(asyncio.Protocol):
    host_header_regex = re.compile(b"^Host: (.*)\r\n", re.M)
    content_length_regex = re.compile(b"^Content-Length: ([\\d]+)\r\n", re.M)

    def __init__(self, server):
        self.server = server
        self.buf = b""

    def handle_repo(self, data):
        match = self.host_header_regex.search(data)
        if match:
            host = match.group(1).decode()
            asyncio.create_task(self.run_fossil(host, data))

    async def run_fossil(self, host, data):
        try:
            cmd = self.server.get_repo(host, data)
        except BadHost:
            response = b"HTTP/1.0 400 Bad Request\r\n\r\n"
        except Redirect as r:
            response = f"HTTP/1.0 302 Found\r\nLocation: {r.url}\r\n\r\n".encode("utf8")
        else:
            remote_addr = self.transport.get_extra_info("peername")[0]
            args = [cmd[1]] + ["--ipaddr", remote_addr] + cmd[2:]
            env = {"REMOTE_HOST": remote_addr}
            proc = await asyncio.create_subprocess_exec(
                cmd[0],
                *args,
                stderr=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE,
                env=env,
            )
            response, stderr = await proc.communicate(data)
            if stderr:
                print(stderr)

        self.transport.write(response)
        self.transport.write_eof()
        self.buf = b""

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.buf += data
        end_idx = self.buf.index(b"\r\n\r\n")
        if end_idx != -1:
            clen_match = self.content_length_regex.search(self.buf)
            if clen_match:
                content_length = int(clen_match.group(1).decode())
                # print(f"Content-Length: {content_length}")
                found_len = len(self.buf[end_idx:])
                if found_len < content_length:
                    # print(f"Need to buffer {content_length} -> {found_len}")
                    return
            self.handle_repo(self.buf)

    def connection_lost(self, exc):
        pass


class FossilDirector:
    def __init__(self, config_file):
        self.config, self.repos = self.configure(config_file)

    async def start(self):
        loop = asyncio.get_event_loop()
        server = await loop.create_server(
            lambda: HttpProtocol(self),
            self.config.get("server", "host"),
            self.config.get("server", "port"),
        )

        async with server:
            try:
                await server.serve_forever()
            except asyncio.exceptions.CancelledError:
                await server.wait_closed()
                return

    def get_repo(self, hostname: str, request: bytes) -> list[str]:
        args, root_redirect = self.repos.get(hostname, (None, None)) or self.repos.get(
            "DEFAULT", (None, None)
        )
        if args:
            if root_redirect:
                if request.split(b"\r\n")[0].split(b" ")[1] == b"/":
                    raise Redirect(root_redirect)
            return args
        else:
            raise BadHost()

    def configure(self, config_file: str):
        from configparser import ConfigParser

        config = ConfigParser()
        config.read_dict(
            {
                "server": {
                    "host": "127.0.0.1",
                    "port": 7000,
                    "fossil_cmd": "/usr/local/bin/fossil",
                }
            }
        )
        config.read(config_file)
        repos = {}

        for section in config.sections():
            if section != "server":
                args = [config.get("server", "fossil_cmd"), "http"]
                base_url = config.get(section, "baseurl", fallback="")
                if base_url:
                    args.extend(["--baseurl", base_url])
                repolist = config.getboolean(section, "repolist", fallback=False)
                if repolist:
                    args.append("--repolist")
                extra_args = config.get(section, "args", fallback="")
                if extra_args:
                    args.extend(extra_args.split(" "))
                args.append(os.path.abspath(config.get(section, "repo")))
                redirect_root = config.get(section, "redirect_root", fallback="")
                repos[section.lower()] = (args, redirect_root)

        print(f"Using fossil: {config.get('server', 'fossil_cmd'):>60s}")
        print("Domains:")
        for host, (info, _) in repos.items():
            print(f"{host:<20s}{info[-1]:>60s}")
        sys.stdout.flush()
        return config, repos


def main():
    if len(sys.argv) < 2:
        print("Usage: fossil-director [CONFIG FILE]")
        sys.exit(-1)
    config_file = sys.argv[1]
    if not os.path.exists(config_file):
        print(f"{config_file} does not exist")
        sys.exit(-1)

    server = FossilDirector(config_file)
    asyncio.run(server.start())


if __name__ == "__main__":
    main()
