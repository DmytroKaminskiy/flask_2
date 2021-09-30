import string
import random


def generate_password(num: int = 10) -> str:

    if num <= 0:
        raise TypeError(f'Num should be greater than 0.')

    chars = string.ascii_letters + string.digits

    result = ''

    for _ in range(num):
        result += random.choice(chars)

    return result
