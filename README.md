# scrmbl <a href="https://coveralls.io/github/etienne-napoleone/scrmbl?branch=develop"><img align="right" src="https://coveralls.io/repos/github/etienne-napoleone/scrmbl/badge.svg?branch=develop"></a> <a href="https://travis-ci.org/etienne-napoleone/scrmbl"><img align="right" src="https://travis-ci.org/etienne-napoleone/scrmbl.svg?branch=develop"></a>

Library and CLI for "scrambled" printing in terminal.

Have you ever wanted to print your text like some corny action movies?

<p align="center">
  <img width="75%" src="https://raw.githubusercontent.com/etienne-napoleone/scrmbl/develop/demo.gif"></a>
</p>

note: the `%` are coming from my tty recorder

## Requirements

- Tested on Python >= 3.5

## Install

### CLI

```
pip3 install --user scrmbl
```

### Library

Using pip in a virtualenv.

```bash
pip install scrmbl
```

Using Poetry:

```bash
poetry add scrmbl
```

Using Pipenv:

```bash
pipenv install scrmbl
```

## Usage

Refer to the gif to see the effect

### CLI

```
Usage: scrmbl [OPTIONS] [MESSAGE]

  Scrmbl print the given message.

Options:
  -s, --speed FLOAT         Time in seconds between prints. Default: 0.05
  -i, --iterations INTEGER  Number of iterations per character. Default: 2
  -c, --charset FILE        Set of chars to scramble.
  --version                 Show the version and exit.
  --help                    Show this message and exit.
```

Can also read from stdin.

```bash
ls -lrtha | scrmbl
```

## Library

```python
>>> import scrmbl

>>> scrmbl.echo('09:30pm, Washington, NSA HEADQUARTERS')
'09:30pm, Washington, NSA HEADQUARTERS'

# handle multiline
>>> scrmbl.echo('09:30pm, Washington\nNSA HEADQUARTERS')
'02:56am, New-York'
'FBI HEADQUARTERS'

# custom settings:
# charset = String of characters to scramble with
# speed = Time in seconds between prints
# iterations = number of iterations before printing the final character
>>> scrmbl.echo('NSA OFFICE', charset='ABCDefg/-', speed=0.2, iterations=6)
'CIA OFFICE'
```

## Thanks

Special thanks for contributing:
- [@podstava](https://github.com/podstava)
- [@0jdxt](https://github.com/0jdxt)
