import hash_functions
import argparse
import sys
import time
import csv

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
                print("hash_and_slot", start_hash % self.N, self.M) 
                self.M += 1
                return True
        return False

    def search(self, key):
        # Our initial spot to search will be from the hash function
        # output
        start_hash = self.hash_function(key, self.N)
        for i in range(self.N):
            # Starting at the hash slot, look to see whether the key matches
            # the value. If not, look at the next spot
            slot = (start_hash + i) % self.N
            if self.T[slot] == None:
                # If the slot is empty, it means the key was never added
                return None
            if key == self.T[slot][0]:
                return self.T[slot][1]
        return None

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="explores the efficiency of various hashing strategies")
    parser.add_argument("--probe_type",
                        help="Linear or Chained Hash add/search strategy", type=str)
    parser.add_argument("--hash_type",
                        help="rolling or ascii hash function",
                        type=str)
    parser.add_argument("--table_size", help="size of word list", type=int)
    parser.add_argument("--key_file", help="keys to add to hash table", type=str)
    parser.add_argument("--number_of_keys", help="number of keys to add from the file", type=str)
    
    r = None
    args = parser.parse_args()
    
    if args.probe_type == "linear":
        if args.hash_type == 'ascii':
            r = LinearProbe(args.table_size, hash_functions.h_ascii)
        if args.hash_type == 'rolling':
            r = LinearProbe(args.table_size, hash_functions.h_rolling)
    else:
        print("probe strategy not recognized!")
        sys.exit()
    
    for l in open(args.key_file):
        t0 = time.time()
        r.add(l, l)
        t1 = time.time()
        print('add_time', r.M/r.N, t1-t0)
        if r.M == args.number_of_keys:
            break

    for m in open(args.key_file):
        t0 = time.time()
        search_val = r.search(m)
        t1 = time.time()
        print('search', t1-t0)
