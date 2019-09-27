import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
        loc2 = Location("Cal_poly", 12.1, -123.7)
        self.assertEqual(repr(loc2), "Location('Cal_poly', 12.1, -123.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Cal_poly", 12.1, -123.7)
        loc3 = Location("Cal_poly", 12.1, -123.7)
        loc4 = loc

        self.assertTrue(loc == loc4)
        self.assertFalse(loc == loc2)
        self.assertTrue(loc2 == loc3)


if __name__ == "__main__":
    unittest.main()
