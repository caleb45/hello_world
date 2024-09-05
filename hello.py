import numpy as np 
import pandas as pd 

print(np.__version__) 
print(pd.__version__)

print('hello world!!')


arr1 = np.array(range(1, 11))
arr2 = np.array(range(1, 11, 2))

print(f'arr1 : {arr1}')
print(f'arr2 : {arr2}')


arr1 = np.array(range(1, 11))
arr2 = np.array(range(11, 21))
arr3 = arr1 + arr2 
print('arr1 + arr2 : {arr3}')



print(f'-------------------------------')
print(f'Numpy Operation Example')

# Slicing Numpy Arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2,3,4,5
print(np1[1:5])

# Return from something till the end of the array?
# 4-9
print(np1[3:])

# Return Negative Slices
# 7, 8
print(np1[-3:-1])

# Steps
print(np1[1:5]) # 2-5
print(np1[1:5:2]) # 2-5 in steps of 2

# Steps on the enitre array
print(np1[::2])
print(np1[::3])

# Slice a 2-d array
np2 = np.array([
        [1,2,3,4,5],
        [6,7,8,9,10]])
# Pull out a single item
print(np2[1,2])

# Slice a 2-d array 2,3
print(np2[0:1, 1:3])



