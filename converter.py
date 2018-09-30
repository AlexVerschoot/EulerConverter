'''
Created on Sep 30, 2018

@author: alex
'''

from math import sin, cos
from math import radians

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
    pass