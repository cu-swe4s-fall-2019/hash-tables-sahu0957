import unittest
import hash_tables
import hash_functions
import random
import statistics
import math

r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
r.add('sample1', 'value1')
x = r.search('sample1')
#self.assertEqual(r.search('sample1'), 'value1')
print(x)


class TestHashTables(unittest.TestCase):
 
    def test_hash_table_ascii_add(self):
        # We  add one word to a table of size 1, which should end
        # up at index 0 regardless of its hash
        r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.T[0], ('sample1', 'value1'))

    def test_hash_table_search(self):
        r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.search('sample1'), 'value1')

    def test_hash_table_full(self):
        # If the hash table is full, it should submit an error
        r = hash_tables.LinearProbe(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.add('sample2', 'value2'), False)

    def test_hash_table_search_last_index(self):
        # A test to make sure the last index is return the expected value
        r = hash_tables.LinearProbe(5, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        r.add('sample2', 'value2')
        r.add('sample3', 'value3')
        r.add('sample4', 'value4')
        r.add('sample5', 'value5')
        self.assertEqual(r.search('sample5'), 'value5')
    
    def test_hash_table_search_rolling(self):
        # A test to see if we will return the proper value when hashing
        # Using the rolling polynomial strategy
        r = hash_tables.LinearProbe(5, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        r.add('sample2', 'value2')
        r.add('sample3', 'value3')
        r.add('sample4', 'value4')
        r.add('sample5', 'value5')
        self.assertEqual(r.search('sample5'), 'value5')

if __name__ == '__main__':
    unittest.main()

