import hash_functions

class LinearProbe:
    def __init__(self, N, hash_function):
        # Specify hash function to use (h_ascii or h_rolling)
        self.hash_function = hash_function
        
        # Specify table size
        self.N = N

        # initiate a table of size N populated with None
        self.T = [None for i in range(N)]
        
        # Define a load factor for rehashing
        self.M = 0

    def add(self, key, value):
        
        # Define a starting value in the table. If this
        # Index is full already, we'll move on to the next empty
        # slot linearly
        start_hash = self.hash_function(key, self.N)
        for i in range(self.N):
            # Increase the start hash incrementally (only if the
            # first hash slot is already filled)
            slot = (start_hash + i) % self.N
            if self.T[slot] == None:
                self.T[slot] = (key, value)
                self.M += 1
                return True 

        print(self.M)
        print("the hash table is full!")
        return False

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        pass

class ChainedHash:
    def __init__(self, N, hash_fucntion):
        self.hash_fucntion = hash_fucntion
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_fucntion(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_fucntion(key, self.N)
        pass


