# EulerConverter
Convert any sequence of euler/Tait–Bryan angles into a ZXZ euler angle. Completely written in python. The only depency is math.

Example code :
from converter import toMatrix
inputAngles = (60,30,0)
result = toMatrix.convertEulerToZXZ("Z", "X", "Z", inputAngles[0], inputAngles[1], inputAngles[2])
