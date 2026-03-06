import numpy as np 

arr_2d = np.array([[1,2],[3,4]])

# insert a new row at index 1 
''''
axis=0 it is in row wise 
axis=1 it is in coloumn wise 
axis=None it is a single line element 

'''
new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)
print(new_arr_2d)