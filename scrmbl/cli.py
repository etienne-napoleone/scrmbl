import sys

import click

from scrmbl.main import echo
import scrmbl.version


@click.command()
@click.argument('text_in', default='')
@click.option('-s', '--speed', type=click.FLOAT, default=0.05,
              help='Time in seconds between prints. Default: 0.05')
@click.option('-i', '--iter', 'niter', type=click.INT, default=2,
              help='Number of iterations per character. Default: 2')
@click.option('-c', '--chars', type=click.Path(
    exists=True, allow_dash=True, dir_okay=False,
), help='Set of chars to scramble.')
@click.version_option(version=scrmbl.version.__version__)
def cli(text_in: str, speed: float, niter: int, chars: str):
    """Scrmbl print the given message."""
    if not text_in:  # no text input
        if sys.stdin.isatty() or chars == '-':  # if no stdin or just '-c -'
            raise click.UsageError('Need TEXT_IN or stdin input.')

        for line in sys.stdin:
            text_in += line

    if chars:
        with click.open_file(chars) as f:
            charset = f.read()
    else:
        charset = ''

    echo(text_in.strip(), charset=charset, speed=speed, iterations=niter)


# for debugging >.\cli.py testing
# if __name__ == '__main__':
#     cli()
