# EulerConverter
Convert any sequence of Euler/Tait–Bryan angles into a ZXZ euler angle. Completely written in python. The only depency is math.

Example code :
```python
from converter import toMatrix
inputAngles = (60,30,0)
result = toMatrix.convertEulerToZXZ("Z", "X", "Z", inputAngles[0], inputAngles[1], inputAngles[2])

outputAngleZ1 = result[0]
outputAngleX2 = result[1]
outputAngleZ3 = result[2]
```
