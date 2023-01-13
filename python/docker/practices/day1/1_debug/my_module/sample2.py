import hashlib


def add(x, y):
    z = x + y
    return z


def hash(x):
    hs = hashlib.md5(x.encode()).hexdigest()
    return hs
