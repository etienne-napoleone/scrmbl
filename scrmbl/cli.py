import sys

import click

import scrmbl


@click.command()
@click.argument('message', default='')
@click.option('-s', '--speed', type=click.FLOAT, default=0.05,
              help='Time in seconds between prints. Default: 0.05')
@click.option('-i', '--iterations', type=click.INT, default=2,
              help='Number of iterations per character. Default: 2')
@click.option('-c', '--charset',
              type=click.Path(exists=True, allow_dash=True, dir_okay=False),
              help='Set of chars to scramble.')
@click.version_option(version=scrmbl.__version__)
def cli(message: str, speed: float, iterations: int, charset: str) -> None:
    """Scrmbl print the given message."""
    # no text input
    if not message:
        # if no stdin or just '-c -'
        if sys.stdin.isatty() or charset == '-':
            raise click.UsageError('"MESSAGE" is empty. No argument or stdin.')
        for line in sys.stdin:
            message += line
    if charset:
        with click.open_file(charset) as f:
            charset_content = f.read()
        charset_content = charset_content.replace('\n', '')
    else:
        charset_content = None
    scrmbl.echo(message.strip(), charset=charset_content, speed=speed,
                iterations=iterations)
