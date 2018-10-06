import random
import string
import time


random.seed()

ALL_CHARS = string.digits + string.ascii_letters + string.punctuation


def echo(message: str, charset: str = ALL_CHARS, speed: float = 0.05,
         iterations: int = 2) -> None:
    "scrmbl print the given message"
    for line in message.split('\n'):
        echoed = ''
        for character in line:
            for iteration in range(iterations):
                print('\r{}{}'.format(echoed, random.choice(charset)), end='')
                time.sleep(speed)
            print('\r{}{}'.format(echoed, character), end='')
            echoed = echoed + character
        print()
