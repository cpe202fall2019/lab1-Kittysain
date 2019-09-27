import unittest
import sample

class TestLab1(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(sample.factorial(0),1)
        self.assertEqual(sample.factorial(1),1)
        self.assertEqual(sample.factorial(2),2)
        self.assertEqual(sample.factorial(6),720)

    def test_fib(self):
        self.assertEqual(sample.fib(0),0)
        self.assertEqual(sample.fib(1),1)
        self.assertEqual(sample.fib(2),1)
        self.assertEqual(sample.fib(6),8)

    def test_maxlist_rec(self):
        tlist = [10, 9, 8, 4, 9]
        self.assertEqual(sample.maxlist_rec(tlist),10)
        tlist = [9, 8, 10, 4, 9]
        self.assertEqual(sample.maxlist_rec(tlist),10)
        tlist = [5, 9, 8, 4, 10]
        self.assertEqual(sample.maxlist_rec(tlist),10)
        tlist = [-10, -9, -1, -4, -9]
        self.assertEqual(sample.maxlist_rec(tlist),-1)
        tlist = []
        with self.assertRaises(ValueError):  # uses context manager to check exception
            sample.maxlist_rec(tlist)
        self.assertRaises(ValueError, sample.maxlist_rec, tlist) # another way to check exception

        # when items in list are all the same
        tlist = [2, 2, 2, 2, 2]
        self.assertEqual(sample.maxlist_rec(tlist), 2)

        # when there is negative and positive values in the list
        tlist = [-2, -4, 1, -1, 0]
        self.assertEqual(sample.maxlist_rec(tlist), 1)


    def test_reverse_iter(self):
        # this test if the function can reverse an empty string
        self.assertEqual(sample.reverse_iter(""),"")
        # this test if the function can reverse a simply string with letters
        self.assertEqual(sample.reverse_iter("abcd"),"dcba")
        # test the reverse function with a mixed of input
        self.assertEqual(sample.reverse_iter("123abcd"), "dcba321")
        self.assertEqual(sample.reverse_iter("123 _abcd"), "dcba_ 321")
        self.assertEqual(sample.reverse_iter("+ = -"), "- = +")
if __name__ == '__main__': 
    unittest.main()
