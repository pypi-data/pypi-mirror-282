# Fossil Director

Fossil-director is an HTTP server used to host multiple [Fossil](https://fossil-scm.org) repositories, based on the hostname.

The server is meant to run behind nginx or other reverse proxy. Fossil-director will inspect the incoming HTTP `Host:` header and dispatch to the configured fossil repository.

## Installation

(Requires Python >= 3.8)

`pip install fossil-director`

## Configuration

A configuration `.ini` is required. At minimum, define a hostname and path to the fossil repository:

```ini
[example.com]
repo = /path/to/repo.fossil
```

Each virtual host is a new section. Here are all of the options:
```ini
[foo.org]
repo = /other/path.fossil
repolist = false                  # if repo is a directory, set this to true to serve 
                                  # a directory index of fossil files
baseurl = http://foo.org/fossil/  # base url
args = --nodelay --acme           # extra arguments to the `fossil http` command
redirect_root = /some/other/path  # redirect requests for / to the given URI
```

By default, the server runs on port 7000. Here are the server options:

```ini
[server]
host = 127.0.0.1
port = 7000
fossil_cmd = /usr/local/bin/fossil  # path to fossil executable

```

## Running

`fossil-director /path/to/config.ini`

Here's an [example systemd service](/file?name=fossil-director.service)


