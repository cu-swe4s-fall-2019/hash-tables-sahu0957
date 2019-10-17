import sys

def h_ascii(key, N):
    # Takes a strng "key" and a table of size N
    # and returns a hash index result
    s = 0
    if key == None:
        raise TypeError("key provided is a None value!")
        sys.exit(1)
    if type(key) != str:
        raise TypeError("key provided is not a string!")
        sys.exit(1)
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_rolling(key, N, p=53, m=2**64):
    # Takes a string "key" and calculates its ascii
    # value, multiplied by a polynomial of 53, which should
    # help prevent collisions
    s = 0
    if key == None:
        raise TypeError("key provided is a None value!")
        sys.exit(1)
    if type(key) != str:
        raise TypeError("key provided is not a string!")
        sys.exit(1)
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s = s % m
    return s % N
