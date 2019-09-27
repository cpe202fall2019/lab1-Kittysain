import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # this test case check when the list is none
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        # this test case check when the list is empty with no value
        self.assertEqual(max_list_iter([]), None)

        # these test cases check when the list has items that are all the same
        self.assertEqual(max_list_iter([1, 1, 1, 1]), 1)

        # these test cases check when the list contain only 1 maximum number at different positions
        self.assertEqual(max_list_iter([1, 1, 1, 2]), 2)
        self.assertEqual(max_list_iter([1, 1, 2, 1]), 2)
        self.assertEqual(max_list_iter([1, 2, 1, 1]), 2)
        self.assertEqual(max_list_iter([2, 1, 1, 1]), 2)

        # these test cases check if there are more than 1 maximum number at different positions
        self.assertEqual(max_list_iter([2, 2, 1, 1]), 2)
        self.assertEqual(max_list_iter([1, 2, 2, 1]), 2)
        self.assertEqual(max_list_iter([1, 1, 2, 2]), 2)
        self.assertEqual(max_list_iter([2, 1, 1, 2]), 2)
        self.assertEqual(max_list_iter([2, 1, 2, 1]), 2)

    def test_reverse_rec(self):
        # check the output when the list is none
        rev_list = None
        with self.assertRaises(ValueError):
            reverse_rec(rev_list)
        # test the reverse list with different item
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1, 2, 2, 3, 4, 5]), [5, 4, 3, 2, 2, 1])
        # test when all of the item in the list is the same
        self.assertEqual(reverse_rec([1, 1, 1]), [1, 1, 1])
        # test when there is no item in the list
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(3, 0, len(list_val) - 1, list_val), 3)

        # test when the list has an odd number of items
        list_val2 = [20, 22, 24, 36, 102, 188, 200]
        self.assertEqual(bin_search(20, 0, len(list_val2) - 1, list_val2), 0)
        self.assertEqual(bin_search(102, 0, len(list_val2) - 1, list_val2), 4)
        self.assertEqual(bin_search(188, 0, len(list_val2) - 1, list_val2), 5)
        self.assertEqual(bin_search(200, 0, len(list_val2) - 1, list_val2), 6)

        # test when target is not in the list
        self.assertEqual(bin_search(-1, low, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(20, low, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(10, low, len(list_val2) - 1, list_val2), None)

        # test when the list is None
        empty_list = None
        with self.assertRaises(ValueError):
            bin_search(2, 1, 2, empty_list)


if __name__ == "__main__":
    unittest.main()
