# Almost Even

"""


"""

import unittest
from collections import defaultdict
import time

# My Solution

def split_integer(num, parts):
    divisor = num//parts
    num_parts = []
    
    for i in range(parts):
        num_parts.append(divisor)
        num -= divisor
        parts -= 1
        try:
            divisor = num//parts
        except:
            return num_parts
        
    return num_parts

# Other Solutions

def splitInteger(num,parts):
    res = []
    for q in range(parts):
        res.append(num / parts)
        num -= num / parts
        parts -= 1
    return res

# Test Cases

class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(split_integer(10, 1), [10])
        print('PASSED')
    def test_case_2(self):
        self.assertEqual(split_integer(2, 2), [1, 1])
        print('PASSED')
    def test_case_3(self):
        self.assertEqual(split_integer(20 , 5), [4, 4, 4, 4, 4])
        print('PASSED')

if __name__ == '__main__':
    unittest.main()