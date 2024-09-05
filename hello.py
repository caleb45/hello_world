import numpy as np 
import pandas as pd 

print(np.__version__) 
print(pd.__version__)

print('hello world!!')


arr1 = np.array(range(1, 11))
arr2 = np.array(range(1, 11, 2))

print(f'arr1 : {arr1}')
print(f'arr2 : {arr2}')

print(f'--------------------')
print(f'Pandas Code Added')

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]).T, columns=['A', 'B', 'C'])
print('dataframe : ')
print(df)

