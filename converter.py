'''
Created on Sep 30, 2018

@author: alex
'''

from math import sin, cos, asin, acos
from math import radians, degrees

class matrixOperations():
    """
    A class that countains a matrix multiplication algoritm. Didn't use numpy to keep the depencies to math
    """
    @staticmethod
    def matrixmult (A, B):
        """
        Multiply matrix A (double[x][y]) with matrix B (double[y],[Z])
        """
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
        Transforms an X angle in it's 3x3 rotation matrix.  Return will be a double[3][3]
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
        Transforms an Y angle in it's 3x3 rotation matrix.  Return will be a double[3][3]
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
        Transforms an X angle in it's 3x3 rotation matrix. Return will be a double[3][3]
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
        Will return the 3x3 matrix from a certain axis. Return will be a double[3][3]
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
        Give the sequence and the angles in degrees, get the rotation matrix back as a double[3][3]
        @param firstAxis:"X", "Y" or "Z"
        @type firstAxis:char/string
        @param secondAxis:"X", "Y" or "Z"
        @type secondAxis:char/string
        @param thirdAxis:"X", "Y" or "Z"
        @type thirdAxis:char/string
        @param firstAxisAngle:angle in degrees
        @type firstAxisAngle:int/double/float
        @param secondAxisAngle:angle in degrees
        @type secondAxisAngle:int/double/float
        @param thirdAxisAngle:angle in degrees
        @type thirdAxisAngle:int/double/float
        """
        return matrixOperations.matrixmult(matrixOperations.matrixmult(toMatrix.toRotMatrix(firstAxisAngle, firstAxis), toMatrix.toRotMatrix(secondAxisAngle, secondAxis)), toMatrix.toRotMatrix(thirdAxisAngle, thirdAxis))

    @staticmethod
    def convertEulerToZXZ(firstInputAxis, secondInputAxis, thirdInputAxis, firstInputAxisAngle, secondInputAxisAngle, thirdInputAxisAngle):
        """
        Convert any kind of angle into a ZXZ euler angle, will return a the following tuple : (Z,X,Z)
        The results are rounded at 10 digits
        @param firstInputAxis:"X", "Y" or "Z"
        @type firstInputAxis:char/string
        @param secondInputAxis:"X", "Y" or "Z"
        @type secondInputAxis:char/string
        @param thirdInputAxis:"X", "Y" or "Z"
        @type thirdInputAxis:char/string
        @param firstInputAxisAngle:angle in degrees
        @type firstInputAxisAngle:int/double/float
        @param secondInputAxisAngle:angle in degrees
        @type secondInputAxisAngle:int/double/float
        @param thirdInputAxisAngle:angle in degrees
        @type thirdInputAxisAngle:int/double/float
        """
        rotationMatrix = toMatrix.getRotationMatrix(firstInputAxis, secondInputAxis, thirdInputAxis, firstInputAxisAngle, secondInputAxisAngle, thirdInputAxisAngle)
        
        X2rad = acos(rotationMatrix[2][2])
        if X2rad == 0:
            return (degrees(acos(rotationMatrix[0][0])),0,0)
        Z1rad = asin(rotationMatrix[0][2]/sin(X2rad))
        #round because of floating point errors causing math errors
        Z3rad = acos(round(rotationMatrix[2][1]/sin(X2rad),10))
        return (round(degrees(Z1rad),10), round(degrees(X2rad),10), round(degrees(Z3rad),10))
        

if __name__ == '__main__':
    
    pass