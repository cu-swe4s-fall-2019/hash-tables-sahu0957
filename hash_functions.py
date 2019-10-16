
def h_ascii(key, N):
    # Takes a strng "key" and a table of size N
    # and returns a hash index result
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_rolling(key, N):
    return None
