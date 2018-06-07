# rotations.py
Rotate an array of points in cartesian coordinates about the x, y, z axis 
or a specified vector by a specified angle.

## Overview
Call functions xrotate, yrotate, zrotate, and vrotate to rotate 3-dimensional
arrays how you need to.

Running rotations.py shows a basic example of how it works. ('python rotations.py') No additional input necessary.

## How-To
positions = [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3],..., [xn, yn, zn]]

theta = ## degrees

vector = [vx1, vx2, vx3]

xrotate(positions, theta)

yrotate(positions, theta)

zrotate(positions, theta)

vrotate(positions, theta, vector)

### Additional Files
#### rotationsVid.py

an example of rotations.py functions at work, showing points
aligned in a cube rotating using each function

#### rotationsTime.py

shows how quickly rotations.py works
Recent approximate run times (may vary by computer):

|Points (#) |Time (s)|
|---|---|
| 100000 | 0.006 |
| 1000000 | 0.023 |
| 10000000 | 0.221 |
| 100000000 | 2.043 |
