import unittest
import hash_tables
import hash_functions
import random

class TestLPHashTables(unittest.TestCase):
 
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
        # If the hash table is full, it should submit a "False"
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

    def test_hash_table_add_rolling_None(self):
        # If we try to add a None object, it should raise an error 
        r = hash_tables.LinearProbe(5, hash_functions.h_rolling)
        with self.assertRaises(TypeError):
            r.add(None, None)
    
    def test_hash_table_add_ascii_None(self):
        # If we try to add a None object, it should raise an error 
        r = hash_tables.LinearProbe(5, hash_functions.h_ascii)
        with self.assertRaises(TypeError):
            r.add(None, None)
    
    def test_hash_table_search_notpresent(self):
        # If we try to add a None object, it should raise an error 
        r = hash_tables.LinearProbe(5, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        r.add('sample2', 'value2')
        self.assertEqual(r.search('sample3'), None)

class TestCHHashTables(unittest.TestCase):
    
    def test_chainedhash_ascii_addone(self):
        # a one-word, one-value key should always go in the first slot
        r = hash_tables.ChainedHash(1, hash_functions.h_ascii)
        r.add('sample1', 'value1')
        self.assertEqual(r.T[0], [('sample1', 'value1')])
    
    def test_chainedhash_rolling_addone(self):
        # a one-word, one-value key should always go in the first slot
        r = hash_tables.ChainedHash(1, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        self.assertEqual(r.T[0], [('sample1', 'value1')])
 
    def test_chainedhash_rolling_add_fulltable(self):
        # two one-word, one-value key should always go in the first slot
        # and a collision will result in the second going to the same spot
        # with a different index
        r = hash_tables.ChainedHash(1, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        r.add('sample2', 'value2')
        self.assertEqual(r.T[0][1], ('sample2','value2'))
    
    def test_chainedhash_ascii_search_singleentry(self):
        # search should return value of single entry input
        r = hash_tables.ChainedHash(1, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        self.assertEqual(r.search('sample1'), 'value1')

    def test_chainedhash_ascii_search_notpresent(self):
        # search should return value None when key isn't present
        r = hash_tables.ChainedHash(1, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        self.assertEqual(r.search('sample2'), None)


    def test_chainedhash_ascii_search_last(self):
        # search should return value of the last sample added
        r = hash_tables.ChainedHash(1, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        r.add('sample2', 'value2')
        r.add('sample3', 'value3')
        r.add('sample4', 'value4')
        r.add('sample5', 'value5')
        
        self.assertEqual(r.search('sample5'), 'value5')

    def test_chanedhash_collision(self):
        # in a table of 1, all samples will hash to the same spot
        # search should return the values regardless of this
        r = hash_tables.ChainedHash(1, hash_functions.h_rolling)
        r.add('sample1', 'value1')
        r.add('sample2', 'value2')
        r.add('sample3', 'value3')
        r.add('sample4', 'value4')
        r.add('sample5', 'value5')
        
        self.assertEqual(r.search('sample5'), 'value5')

if __name__ == '__main__':
    unittest.main()

