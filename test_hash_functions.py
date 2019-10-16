import unittest
import hash_functions
import random
import statistics
import math

class TestHashFunctions(unittest.TestCase):

    def test_hash_ascii_index1(self):
        # We can test a known ascii hash, such as the word "dog", with a
        # Table size of one, which should have an index of 0 (the first spot)
        r = hash_functions.h_ascii('dog', 1)
        self.assertEqual(r, 0)

    def test_hash_ascii_index313(self):
        # Test a known ascii hash (dog), which has a total sum of 314
        # Tables of size 313 should fit this in slot 1
        r = hash_functions.h_ascii('dog', 313)
        self.assertEqual(r, 1)

    def test_hash_rolling_index1(self):
        # A table of size 1 should always return an index of 0 with one
        # word regardless of size
        r = hash_functions.h_rolling('dog', 1)
        self.assertEqual(r, 0)

    def test_hash_rolling_largetable(self):
        # The resulting hash value for 'dog' is 295310 for this polynomial
        # of 53, so a table of size 295309 should return an index of 1
        r = hash_functions.h_rolling('dog', 295309)
        self.assertEqual(r, 1)
    
if __name__ == '__main__':
    unittest.main()

