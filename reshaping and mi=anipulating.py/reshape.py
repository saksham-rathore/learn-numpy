'''
reshape(rows, coloumns) specify new sahpe
if dimention match
reshaping does not create copy it returns view
'''
import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)