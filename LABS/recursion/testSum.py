import unittest
import recSum 

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(recSum.getSum([1,2,3,4],len([1,2,3,4])-1), 10)
    def test_type(self):
        self.assertIsInstance(recSum.getSum([1,2,3,4],len([1,2,3,4])-1), int)

if __name__ == "__main__":
    unittest.main()   