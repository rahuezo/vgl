import random

KEY_LENGTH = 6
USERS = 1000


def generate():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    key = ''

    while len(key) < KEY_LENGTH:
        key += random.choice(chars)

    return key





