import random
import time
from typing import List

from scrmbl import charsets

random.seed()


def echo(message: str, charset: List[str] = charsets.ALL, speed: float = 0.05,
         iterations: int = 2):
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
