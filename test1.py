# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:28:56 2021

@author: LiYX
"""

import unittest
from hw1 import sum1,sum2
 
 
class TestA(unittest.TestCase):
    def testsum1(self):
        num1 = [-2,  11, -4, 13, -5, -2]
        num2 = [1, 2, 3]
        num3 = [-1, -2]
        num4 = [1]
        self.assertEqual(sum1(num1), 20)
        self.assertEqual(sum1(num2), 6)
        self.assertEqual(sum1(num3), 0)
        self.assertEqual(sum1(num4), 1)
    def testsum2(self):
        numbers1=[[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6],[-1,-2,-3,1,-4]]
        numbers2=[[1,1,1,1,1],[1,2,3,4,5],[5,4,2,1,3],[3,4,7,5,8],[3,5,9,6,1]]
        numbers3=[[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1],[-2,3,3,3,-2],[-3,3,3,3,-2]]
        numbers4=[[0,-1,-1,-2,-3],[-4,-5,-6,-7,-9],[-3,-4,-9,-6,-2],[-3,-4,-8,-3,-2],[-2,-5,-6,-7,-2]]
        self.assertEqual(sum2(numbers1,5,5), 29)
        self.assertEqual(sum2(numbers2,5,5), 86)
        self.assertEqual(sum2(numbers3,5,5), 18)
        self.assertEqual(sum2(numbers4,5,5), 1)
 
 
if __name__ == '__main__':
    unittest.main()