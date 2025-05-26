import numpy as np
import time
size = 1000000
list1 = range(size)
list2 = range(size)
start = time.time()
r = [x+y for x, y in zip(list1, list2)]
end = time.time()
print("list time:- ", end-start)
array1 = np.arange(size)
array2 = np.arange(size)
start = time.time()
r = array1+array2
end = time.time()
print("array time:- ", end- start)