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
    for line in message.split('\n'):
        echoed = ''
        for char in line:
            for _ in range(iterations):
                if char != ' ':
                    ran_char = random.choice(charset)
                    click.echo('\r{}{}'.format(echoed, ran_char), nl=False)
                else:
                    click.echo('\r{}'.format(echoed), nl=False)
                time.sleep(speed)
            echoed += char
            # wrap if line longer than console cols
            if len(echoed) >= COLS - 1:
                click.echo('\r' + echoed)
                echoed = ''
        if echoed:
            click.echo('\r' + echoed)
