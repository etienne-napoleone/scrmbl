from typing import List
import random
import time

from scrmbl import charsets

random.seed()


def echo(message: str, charset: List[str] = charsets.ALL, speed: float = 0.05,
         iterations: int = 2):
    "scrmbl print the given message"
    echoed = ''
    for character in message:
        for iteration in range(iterations):
            print('\r{}{}'.format(echoed, random.choice(charset)), end='')
            time.sleep(speed)
        print('\r{}{}'.format(echoed, character), end='')
        echoed = echoed + character
    print()
