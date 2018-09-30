'''
Created on Sep 30, 2018

@author: alex
'''

from math import sin, cos
from math import radians

class matrixOperations():
    @staticmethod
    def matrixmult (A, B):
        C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k]*B[k][j]
        return C

class toMatrix():
    @staticmethod
    def toRotXMatrix(angleInDegrees):
        """
        Transforms an X angle in it's 3x3 rotation matrix
        @param angleInDegrees: angle in degrees
        @type angleInDegrees:int/double/float
        """
        angleInRadians = radians(angleInDegrees)
        return [
            [1,0,0],
            [0, cos(angleInRadians), -sin(angleInRadians)],
            [0, sin(angleInRadians), cos(angleInRadians)]
            ]
        
    @staticmethod
    def toRotYMatrix(angleInDegrees):
        """
        Transforms an Y angle in it's 3x3 rotation matrix
        @param angleInDegrees: angle in degrees
        @type angleInDegrees:int/double/float
        """
        angleInRadians = radians(angleInDegrees)
        return [
            [cos(angleInRadians), 0, sin(angleInRadians)],
            [0,1,0],
            [-sin(angleInRadians), 0, cos(angleInRadians)]
            ]
        
    @staticmethod
    def toRotZMatrix(angleInDegrees):
        """
        Transforms an X angle in it's 3x3 rotation matrix
        @param angleInDegrees: angle in degrees
        @type angleInDegrees:int/double/float
        """
        angleInRadians = radians(angleInDegrees)
        return [
            [cos(angleInRadians), -sin(angleInRadians), 0],
            [sin(angleInRadians), cos(angleInRadians),0],
            [0,0,1]
            ]

if __name__ == '__main__':
    #print(toMatrix.toRotXMatrix(90)*toMatrix.toRotYMatrix(90))
    
    pass