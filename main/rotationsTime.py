#To test how fast rotations.py is
from rotations import *
import numpy as np
from timeit import default_timer as timer

ranx5 = np.random.randint(10,size=(100000,3))
ranx6 = np.random.randint(10,size=(1000000,3))
ranx7 = np.random.randint(10,size=(10000000,3))
ranx8 = np.random.randint(10,size=(100000000,3))

start = timer()
vrotate(ranx5, 40, [4,2,3])
end = timer()
timex5 = end-start

start = timer()
vrotate(ranx6, 40, [4,2,3])
end = timer()
timex6 = end-start

start = timer()
vrotate(ranx7, 40, [4,2,3])
end = timer()
timex7 = end-start

start = timer()
vrotate(ranx8, 40, [4,2,3])
end = timer()
timex8 = end-start

print(timex5, timex6, timex7, timex8)
