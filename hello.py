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
