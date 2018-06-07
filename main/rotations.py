'''
rotations.py rotates cartesian points about x,y,z axis and/or specified vector.
See rotationsVid.py for a more extensive example with outputted graphics with rotations.py at work
'''
#Data array format: [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3],...[xn,yn,zn]]
#Specified vector array: [vx,vy,vz]
#Output array format: [[xr1, yr1, zr1],[xr2,yr2,zr2],[xr3,yr3,zr3],...[xrn,yrn,zrn]]
#Theta (angle) input in degrees

import numpy as np #only requirement

#Rotation definitions
def xrotate(positions, theta): # rotation about the x-axis
    theta = np.deg2rad(theta)
    xr = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
    return np.dot(positions, xr)

def yrotate(positions, theta): # rotation about the y-axis
    theta = np.deg2rad(theta)
    yr = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])
    return np.dot(positions, yr)

def zrotate(positions, theta): # rotation about the z-axis
    theta = np.deg2rad(theta)
    zr = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
    return np.dot(positions, zr)

def vrotate(positions, theta, vec): # rotation about specified vector
    vec = normalize(vec)
    theta = np.deg2rad(theta)
    ux = vec[0]
    uy = vec[1]
    uz = vec[2]
    #Utilize known rotation matrix
    rot = np.array([[np.cos(theta) + ux*ux*(1-np.cos(theta)), ux*uy*(1-np.cos(theta))-uz*np.sin(theta), ux*uz*(1-np.cos(theta))+uy*np.sin(theta)],
                    [uy*ux*(1-np.cos(theta))+uz*np.sin(theta), np.cos(theta) + uy*uy*(1-np.cos(theta)), uy*uz*(1-np.cos(theta))-ux*np.sin(theta)],
                   [uz*ux*(1-np.cos(theta))-uy*np.sin(theta), uz*uy*(1-np.cos(theta))+ux*np.sin(theta), np.cos(theta)+uz*uz*(1-np.cos(theta))]])
    return np.dot(positions, rot)

def normalize(vec): #normalize function used in vrotate
    norm = np.linalg.norm(vec)
    return vec/norm

def main():
    #Example code of how to run
    print("Example of 4 points")
    a = np.random.randint(10,size=(4,3))
    print("Array = \n {}".format(a))
    theta = 45
    print("Theta = {} deg".format(theta))
    xrot = xrotate(a, theta)
    yrot = yrotate(a,theta)
    zrot = zrotate(a, theta)
    vec = [1,1,1]
    vrot = vrotate(a, theta, vec)
    print("x-rotation array = \n{}".format(xrot))
    print("y-rotation array = \n{}".format(yrot))
    print("z-rotation array = \n{}".format(zrot))
    print("v-rotation about vector [1,1,1] array = \n{}".format(vrot))

if __name__ == "__main__":
    main()
