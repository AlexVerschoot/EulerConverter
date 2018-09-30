'''
Created on Sep 30, 2018

@author: alex
'''
import unittest
from math import cos, sin
from converter import toMatrix, matrixOperations

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
    
    def test_matrix_multiplication(self):
        A=[
            [1,2],
            [3,4]
            ]
        B=[
            [2,0],
            [1,2]
            ]
        result=[
            [4,4],
            [10,8]
            ]
        self.assertEqual(matrixOperations.matrixmult(A,B), result, "Matrix multiplication is faulty")
        A=[
            [2,0],
            [1,2]
            ]
        B=[
            [1,2],
            [3,4]
            ]
        result=[
            [2,4],
            [7,10]
            ]
        self.assertEqual(matrixOperations.matrixmult(A,B), result, "Matrix multiplication is faulty")
        A=[
            [1,2,3],
            [4,5,6]
            ]
        B=[
            [9],
            [8],
            [7]
            ]
        result=[
            [46],
            [118]
            ]
        self.assertEqual(matrixOperations.matrixmult(A,B), result, "Matrix multiplication is faulty")
        
        A=[
            [1,3,5,7],
            [2,4,6,8]
            ]
        B=[
            [1,8,9],
            [2,7,10],
            [3,6,11],
            [4,5,12]
            ]
        result=[
            [50,94,178],
            [60,120,220]
            ]
        self.assertEqual(matrixOperations.matrixmult(A,B), result, "Matrix multiplication is faulty")
        
        A=[
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
        B=[
            [10,20,30],
            [40,50,60],
            [70,80,90]
            ]
        result=[
            [300,360,420],
            [660,810,960],
            [1020,1260,1500]
            ]
        self.assertEqual(matrixOperations.matrixmult(A,B), result, "Matrix multiplication is faulty")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()