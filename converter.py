'''
Created on Sep 30, 2018

@author: alex
'''

from math import sin, cos
from math import radians
import re

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
        
    @staticmethod
    def toRotMatrix(angleInDegrees, AxisName):
        """
        Will return the 3x3 matrix from a certain axis
        @param angleInDegrees: angle in degrees
        @type angleInDegrees:int/double/float
        @param AxisName: "X", "Y" or "Z"
        @type AxisName: char/string
        """
        if AxisName == 'X' :
            return toMatrix.toRotXMatrix(angleInDegrees)
        if AxisName == 'Y' :
            return toMatrix.toRotYMatrix(angleInDegrees)
        if AxisName == 'Z' :
            return toMatrix.toRotZMatrix(angleInDegrees)
        else :
            raise ValueError("the axises must be X,Y or Z. An invalid axis was detected")
            
        
    @staticmethod
    def getRotationMatrix(firstAxis, secondAxis, thirdAxis, firstAxisAngle, secondAxisAngle, thirdAxisAngle):
        """
        @param firstAxis:"X", "Y" or "Z"
        @type firstAxis:
        @param secondAxis:"X", "Y" or "Z"
        @type secondAxis:
        @param thirdAxis:"X", "Y" or "Z"
        @type thirdAxis:
        @param firstAxisAngle:angle in degrees
        @type firstAxisAngle:
        @param secondAxisAngle:angle in degrees
        @type secondAxisAngle:
        @param thirdAxisAngle:angle in degrees
        @type thirdAxisAngle:
        """
        return matrixOperations.matrixmult(matrixOperations.matrixmult(toMatrix.toRotMatrix(firstAxisAngle, firstAxis), toMatrix.toRotMatrix(secondAxisAngle, secondAxis)), toMatrix.toRotMatrix(thirdAxisAngle, thirdAxis))


if __name__ == '__main__':
    print(toMatrix.getRotationMatrix("X", "Y", "Z", 5, 10, 15))
    #toMatrix.getRotationMatrix('A','Y','Z', 90,90,90)
    
    pass