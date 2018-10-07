import random
import string
import time

import click

random.seed()

ALL_CHARS = string.digits + string.ascii_letters + string.punctuation
COLS, _ = click.get_terminal_size()


def echo(message: str, charset: str = ALL_CHARS, speed: float = 0.05,
         iterations: int = 2) -> None:
    """Scrmbl print the given message."""
    if not charset:
        charset = ALL_CHARS

    # strip \n and \r from charset
    charset = charset.replace('\n', '').replace('\r', '')

    for line in message.split('\n'):
        echoed = ''
        for char in line:
            for _ in range(iterations):
                ran_char = random.choice(charset)
                click.echo('\r{0}{1}'.format(echoed, ran_char), nl=False)
                time.sleep(speed)
            echoed += char

            # this logic is so lines longer than the console wrap around
            if len(echoed) >= COLS - 1:
                click.echo('\r' + echoed)
                echoed = ''
        if echoed:
            click.echo('\r' + echoed)
