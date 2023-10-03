#!/usr/bin/python3

import unittest
maxInt = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' Tests the max_integer function '''

    def test_standard_list(self):

        list_std = [1, 8, 9, 6, 10]
        self.assertEqual(maxInt(list_std), 10)

    def test_sorted_list(self):

        list_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(maxInt(list_sorted), 9)

    def test_unsorted(self):

        unsorted = [4, 6, 3, 1, 9, 2]
        self.assertEqual(maxInt(unsorted), 9)

    def test_emty(self):

        emty = []
        self.assertEqual(maxInt(emty), None)

    def test_float(self):

        floated = [4.1, 6.6, 3.9, 1.7, 9.8, 2.0]
        self.assertEqual(maxInt(floated), 9.8)

    def test_mixed(self):

        mixed = [4.5, 6.8, 3, 1, 9, 2.3]
        self.assertEqual(maxInt(mixed), 9)

    def test_unsorted(self):

        unsorted = [4, 6, 3, 1, 9, 2]
        self.assertEqual(maxInt(unsorted), 9)

    def test_rand_types(self):
        with self.assertRaises(TypeError):
            maxInt({1, 2}, {3, 4, 5})
        with self.assertRaises(TypeError):
            maxInt({1, 2, 3, 4, 5})
        with self.assertRaises(TypeError):
            maxInt([-10, 0.5, "str", {1, 2}])
        with self.assertRaises(TypeError):
            maxInt([None, True])

    def test_None(self):
        self.assertIsNone(maxInt([]), None)
        self.assertIsNone(maxInt(), None)
        self.assertIsNone(maxInt([None]), None)

if __name__ == '__main__':
    unittest.main()
