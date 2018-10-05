# scrmbl <a href="https://gitter.im/scrmbl/Lobby"><img align="right" src="https://img.shields.io/badge/chat-on%20gitter-%234FB999.svg"></a><a href="https://coveralls.io/github/etienne-napoleone/scrmbl?branch=develop"><img align="right" src="https://coveralls.io/repos/github/etienne-napoleone/scrmbl/badge.svg?branch=develop"></a><a href="https://travis-ci.org/etienne-napoleone/scrmbl"><img align="right" src="https://travis-ci.org/etienne-napoleone/scrmbl.svg?branch=develop"></a>

🕵️ Library for "scrambled" printing in terminal

![demo gif](https://raw.githubusercontent.com/etienne-napoleone/scrmbl/develop/demo.gif)

## Requirements

- Tested on Python >= 3.5

## Install

Using pip in a virtualenv.

```bash
pip install scrmbl
```

Using Poetry:

```bash
poetry add scrmbl
```

Using pipenv:

```bash
pipenv install scrmbl
```

## Usage

```python
>>> import scrmbl

# refer to the gif to see the effect
>>> scrmbl.echo('09:30pm, Washington, NSA HEADQUARTERS')
'09:30pm, Washington, NSA HEADQUARTERS'

# handle multiline
>>> scrmbl.echo('09:30pm, Washington\nNSA HEADQUARTERS')
'09:30pm, Washington'
'NSA HEADQUARTERS'

# custom settings:
# charset = List of characters to randomly iterate through
# speed = Milliseconds to wait between each iteration
# iterations = number of iterations before printing the final character
>>> scrmbl.echo('NSA OFFICE', charset=['N', 'S', 'A'], speed=0.2, iterations=6)
'NSA OFFICE'

# premade charsets:
# LETTERS_LOWER
# LETTERS_UPPER
# FIGURES
# SPECIALS
# LETTERS (LETTERS_LOWER + LETTERS_UPPER)
# ALPHANUMERICS (LETTERS + FIGURES)
# ALL (ALPHANUMERICS + SPECIALS)
>>> scrmbl.echo('NSA OFFICE', charset=scrmbl.charsets.LETTERS)
'NSA OFFICE'
```
