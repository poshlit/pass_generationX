from random import choice
from string import ascii_lowercase, digits, punctuation

def generate(num):
    chars = f'{ascii_lowercase}{digits}{punctuation}'
    result = ''.join(choice(chars) for i in range(num))
    return result

def test(result):
    print(f"You new password: {result}")