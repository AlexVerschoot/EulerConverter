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
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")
        
        angle = 30
        expected_result = [
            [1,0,0],
            [0,0.8660254, -0.5000000],
            [0,0.5000000,  0.8660254]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")
        
        angle = 45
        expected_result = [
            [1,0,0],
            [0.0000000,  0.7071068, -0.7071068],
            [0.0000000,  0.7071068, 0.7071068]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")
        
        angle = 60
        expected_result = [
            [1,0,0],
            [0.0000000,  0.5000000, -0.8660254],
            [0.0000000,  0.8660254,  0.5000000 ]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")
        
        angle = 90
        expected_result = [
            [1,0,0],
            [0,0,-1],
            [0,1,0]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")
        
        angle = 135
        expected_result = [
            [1,0,0],
            [0.0000000, -0.7071068, -0.7071068],
            [0.0000000,  0.7071068, -0.7071068 ]
            ]
        result = toMatrix.toRotXMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotX function invalid" + str(angle) + "°")

        
    def test_to_rot_Y_matrix(self):
        angle = 5
        expected_result = [
            [0.9961947,  0.0000000,  0.0871557],
            [0.0000000,  1.0000000,  0.0000000],
            [-0.0871557,  0.0000000,  0.9961947]
            ]
        result = toMatrix.toRotYMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotY function invalid" + str(angle) + "°")
        
        angle = 30
        expected_result = [
            [0.8660254,  0.0000000,  0.5000000],
            [0.0000000,  1.0000000,  0.0000000],
            [-0.5000000,  0.0000000,  0.8660254]
            ]
        result = toMatrix.toRotYMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotY function invalid" + str(angle) + "°")
        
        angle = 45
        expected_result = [
            [0.7071068,  0.0000000,  0.7071068],
            [0.0000000,  1.0000000,  0.0000000],
            [-0.7071068,  0.0000000,  0.7071068]
            ]
        result = toMatrix.toRotYMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotY function invalid" + str(angle) + "°")
        
        angle = 60
        expected_result = [
            [0.5000000,  0.0000000,  0.8660254],
            [0.0000000,  1.0000000,  0.0000000],
            [-0.8660254,  0.0000000,  0.5000000]
            ]
        result = toMatrix.toRotYMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotY function invalid" + str(angle) + "°")
        
        angle = 90
        expected_result = [
            [0.0000000,  0.0000000,  1.0000000],
            [0.0000000,  1.0000000,  0.0000000],
            [-1.0000000,  0.0000000,  0.0000000]
            ]
        result = toMatrix.toRotYMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotY function invalid" + str(angle) + "°")
        
        angle = 135
        expected_result = [
            [ -0.7071068,  0.0000000,  0.7071068],
            [0.0000000,  1.0000000,  0.0000000],
            [-0.7071068,  0.0000000, -0.7071068]
            ]
        result = toMatrix.toRotYMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotY function invalid" + str(angle) + "°")

    def test_to_rot_Z_matrix(self):
        angle = 5
        expected_result = [
            [0.9961947, -0.0871557,  0.0000000],
            [0.0871557,  0.9961947,  0.0000000],
            [0.0000000,  0.0000000,  1.0000000]
            ]
        result = toMatrix.toRotZMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotZ function invalid" + str(angle) + "°")
        
        angle = 30
        expected_result = [
            [0.8660254, -0.5000000,  0.0000000],
            [0.5000000,  0.8660254,  0.0000000],
            [0.0000000,  0.0000000,  1.0000000]
            ]
        result = toMatrix.toRotZMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotZ function invalid" + str(angle) + "°")
        
        angle = 45
        expected_result = [
            [0.7071068, -0.7071068,  0.0000000],
            [0.7071068,  0.7071068,  0.0000000],
            [0.0000000,  0.0000000,  1.0000000]
            ]
        result = toMatrix.toRotZMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotZ function invalid" + str(angle) + "°")
        
        angle = 60
        expected_result = [
            [0.5000000, -0.8660254,  0.0000000],
            [0.8660254,  0.5000000,  0.0000000],
            [0.0000000,  0.0000000,  1.0000000]
            ]
        result = toMatrix.toRotZMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotZ function invalid" + str(angle) + "°")
        
        angle = 90
        expected_result = [
            [ 0.0000000, -1.0000000,  0.0000000],
            [1.0000000,  0.0000000,  0.0000000],
            [0.0000000,  0.0000000,  1.0000000]
            ]
        result = toMatrix.toRotZMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotZ function invalid" + str(angle) + "°")
        
        angle = 135
        expected_result = [
            [ -0.7071068, -0.7071068,  0.0000000],
            [0.7071068, -0.7071068,  0.0000000],
            [0.0000000,  0.0000000,  1.0000000]
            ]
        result = toMatrix.toRotZMatrix(angle)
        self.assertEqual(round_3x3_matrix(expected_result), round_3x3_matrix(result), "rotZ function invalid" + str(angle) + "°")
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()