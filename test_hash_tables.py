import unittest
import hash_tables
import hash_functions
import random
import statistics
import math

class TestHashTables(unittest.TestCase):

    def test_hash_table_ascii_add(self):
        # We can add one word to a table of size 1, which should end
        # up at index 0 regardless of its hash
        r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.T[0], ('sample1', 'value1'))
    
    def test_hash_table_ascii_add(self):
        # We  add one word to a table of size 1, which should end
        # up at index 0 regardless of its hash
        r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.T[0], ('sample1', 'value1'))

    def test_hash_table_full(self):
        # If the hash table is full, it should submit an error
        r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.add('sample2', 'value2'), False)

if __name__ == '__main__':
    unittest.main()

