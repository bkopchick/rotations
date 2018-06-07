from rotations import * #Import from rotations.py
import numpy as np

#Imports required for visualization
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames

#Declare in array positions (cube arrangement)
positions = np.zeros([27,3])
i=0
k = -2
l = -2
m = -1
while i < 26:
    k=-2
    while k <= 0:
        k+=1
        l=-2
        while l <= 0:
            l +=1
            m=-1
            while m <=1:
                positions[i] = [k,l,m]
                m +=1
                i +=1

def init():
    points1.set_data(positions[:9,0],positions[:9,1])
    points1.set_3d_properties(positions[:9,2])
    points2.set_data(positions[9:18,0],positions[9:18,1])
    points2.set_3d_properties(positions[9:18,2])
    points3.set_data(positions[18:,0],positions[18:,1])
    points3.set_3d_properties(positions[18:,2])
    textx.set_text('x-angle: 0')
    texty.set_text('y-angle: 0')
    textz.set_text('z-angle: 0')
    return points1, points2, points3, textx, texty, textz


#Animation criteria where rotations.py functions are called
#This will rotate about the x-axis, y-axis, z-axis, and [1,1,1] vector
def animate(i):
    if i <= 90:
        anglex = i
        global new
        new = xrotate(positions, i)
        x = new[:9,0]
        y = new[:9,1]
        z = new[:9,2]
        x2 = new[9:18,0]
        y2 = new[9:18,1]
        z2 = new[9:18,2]
        x3 = new[18:,0]
        y3 = new[18:,1]
        z3 = new[18:,2]
        points1.set_data(x,y)
        points1.set_3d_properties(z)
        points2.set_data(x2,y2)
        points2.set_3d_properties(z2)
        points3.set_data(x3,y3)
        points3.set_3d_properties(z3)
        textx.set_text('x-axis: %.1f' % anglex)
    elif i > 90 and i <= 180:
        angley = i - 90
        new = yrotate(new, 1)
        x = new[:9,0]
        y = new[:9,1]
        z = new[:9,2]
        x2 = new[9:18,0]
        y2 = new[9:18,1]
        z2 = new[9:18,2]
        x3 = new[18:,0]
        y3 = new[18:,1]
        z3 = new[18:,2]
        points1.set_data(x,y)
        points1.set_3d_properties(z)
        points2.set_data(x2,y2)
        points2.set_3d_properties(z2)
        points3.set_data(x3,y3)
        points3.set_3d_properties(z3)
        texty.set_text('y-axis: %.1f' % angley)
    elif i>180 and i<=270:
        anglez = i-180
        new = zrotate(new, 1)
        x = new[:9,0]
        y = new[:9,1]
        z = new[:9,2]
        x2 = new[9:18,0]
        y2 = new[9:18,1]
        z2 = new[9:18,2]
        x3 = new[18:,0]
        y3 = new[18:,1]
        z3 = new[18:,2]
        points1.set_data(x,y)
        points1.set_3d_properties(z)
        points2.set_data(x2,y2)
        points2.set_3d_properties(z2)
        points3.set_data(x3,y3)
        points3.set_3d_properties(z3)
        textz.set_text('z-axis: %.1f' % anglez)
    else:
        new = vrotate(new, 1, [1,1,1])
        anglex = (i-270)
        angley = (i-270)*.7
        anglez = (i-270)*.7
        x = new[:9,0]
        y = new[:9,1]
        z = new[:9,2]
        x2 = new[9:18,0]
        y2 = new[9:18,1]
        z2 = new[9:18,2]
        x3 = new[18:,0]
        y3 = new[18:,1]
        z3 = new[18:,2]
        points1.set_data(x,y)
        points1.set_3d_properties(z)
        points2.set_data(x2,y2)
        points2.set_3d_properties(z2)
        points3.set_data(x3,y3)
        points3.set_3d_properties(z3)
        textx.set_text('angle: %.1f' % anglex)
        texty.set_text('vector: (1,1,1)')
        textz.set_text('')
        
    return points1, points2, points3, textx, texty, textz

#Set up the matplotlib figure for plotting
fig = plt.figure()
ax = fig.add_axes([0,0,1,1], projection='3d')
textx = ax.text2D(0.0, .90, '',transform = ax.transAxes)
texty = ax.text2D(0.0,.85,'',transform=ax.transAxes)
textz = ax.text2D(0.0,.80,'',transform=ax.transAxes)

#Define colors of points to make them distinct (more visually pleasing)
points1, = ax.plot([],[],[], 'o', c='r')
points2, = ax.plot([],[],[], 'o', c='b')
points3, = ax.plot([],[],[], 'o', c='g')

#Visualize x, y, z lines
linex = ax.plot([2,-2],[0,0],[0,0], '-')
liney = ax.plot([0,0],[2,-2],[0,0],'-')
linez = ax.plot([0,0],[0,0],[2,-2], '-')

#3d plots limits
ax.set_xlim((-1.5,1.5))
ax.set_ylim((-1.5,1.5))
ax.set_zlim((-1.5,1.5))

#animate it and show it
print('system processing animation...')
anim = animation.FuncAnimation(fig, animate, init_func=init, frames = 510, interval = 100, blit=True)
plt.show()