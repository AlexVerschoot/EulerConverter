'''
Created on Sep 30, 2018

@author: alex
'''
import unittest
from math import cos, sin
from converter import toMatrix

def round_3x3_matrix(inputMatrix):
    return [
            [ '%.7f' % elem for elem in inputMatrix[0] ],
            [ '%.7f' % elem for elem in inputMatrix[1] ],
            [ '%.7f' % elem for elem in inputMatrix[2] ]
            ]

class Test(unittest.TestCase):
    def test_to_rot_x_matrix(self):
        angle = 5
        expected_result = [
            [1,0,0],
            [0,0.9961947,-0.0871557],
            [0,0.0871557,0.9961947]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid 5°")
        
        angle = 30
        expected_result = [
            [1,0,0],
            [0,0.8660254, -0.5000000],
            [0,0.5000000,  0.8660254]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid 30°")
        
        angle = 45
        expected_result = [
            [1,0,0],
            [0.0000000,  0.7071068, -0.7071068],
            [0.0000000,  0.7071068, 0.7071068]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid 45°")
        
        angle = 60
        expected_result = [
            [1,0,0],
            [0.0000000,  0.5000000, -0.8660254],
            [0.0000000,  0.8660254,  0.5000000 ]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid 60°")
        
        angle = 90
        expected_result = [
            [1,0,0],
            [0,0,-1],
            [0,1,0]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid 90°")
        
        angle = 135
        expected_result = [
            [1,0,0],
            [0.0000000, -0.7071068, -0.7071068],
            [0.0000000,  0.7071068, -0.7071068 ]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()