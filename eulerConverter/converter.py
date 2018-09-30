'''
Created on Sep 30, 2018

@author: alex
'''

from math import sin, cos
from math import radians

class toMatrix():
    @staticmethod
    def toRotXMatrix(angleInDegrees):
        angleInDegrees = radians(angleInDegrees)
        return [
            [1,0,0],
            [0, cos(angleInDegrees), -sin(angleInDegrees)],
            [0, sin(angleInDegrees), cos(angleInDegrees)]
            ]

if __name__ == '__main__':
    pass