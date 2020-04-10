import unittest
from stats-group.stats import Calc, MulDiv

class test_stats(unittest.TestCase):

    def test_add(self):
        self.assertEqual(MulDiv(1,2).add_me, 3)
        self.assertTrue(MulDiv(1,2).add_me == 3)
    
    def test_sub(self):
        self.assertEqual(MulDiv(1,2).sub_me, -1)
        self.assertFalse(MulDiv(1,2).sub_me == 3)
    def test_mul(self):
        self.assertEqual(MulDiv(1,2).mul_me, 2)
        self.assertTrue(MulDiv(1,2).mul_me == 2)
    
    def test_div(self):
        self.assertEqual(MulDiv(1,2).div_me, 0.5)
        self.assertFalse(MulDiv(1,2).div_me == 3)


if __name__ == "__main__":
    unittest.main()