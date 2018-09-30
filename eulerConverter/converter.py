'''
Created on Sep 30, 2018

@author: alex
'''

from math import sin, cos
from math import radians

class toMatrix():
    @staticmethod
    def toRotXMatrix(angleInDegrees):
        angleInRadians = radians(angleInDegrees)
        return [
            [1,0,0],
            [0, cos(angleInRadians), -sin(angleInRadians)],
            [0, sin(angleInRadians), cos(angleInRadians)]
            ]
        
    @staticmethod
    def toRotYMatrix(angleInDegrees):
        angleInRadians = radians(angleInDegrees)
        return [
            [cos(angleInRadians), 0, sin(angleInRadians)],
            [0,1,0],
            [-sin(angleInRadians), 0, cos(angleInRadians)]
            ]

if __name__ == '__main__':
    pass