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

if __name__ == '__main__':
    unittest.main()

