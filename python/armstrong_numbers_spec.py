# The code is written as driver code. Can you convert it to Unit Test?
import unittest

from armstrong_numbers import find_armstrong_numbers

class TestArmstrong(unittest.TestCase) :
    
    
    "Testing for 0"
    def test_armstrong_0(self) :
        self.assertEqual(find_armstrong_numbers([0]) == [0]) 
    
    "Testing for 0 - 8"
    def test_armstrong_8(self) :
        self.assertEqual(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])

    "Testing for 0 - 100"
    def test_armstrong_100(self) :
        self.assertEqual(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    "Testing for 0 - 900"
    def test_armstrong_900(self) :
        self.assertEqual(find_armstrong_numbers(list(range(0,900))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])




if __name__ == '__main__':
    unittest.main()