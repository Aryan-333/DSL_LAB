import numpy as np

#2- Dimensional array (Matrix)
a = np.arange(15).reshape(3, 5)
                # array([[ 0, 1, 2, 3, 4],
                # [ 5, 6, 7, 8, 9],
                # [10, 11, 12, 13, 14]])
#to check the dimension
dim = a.shape
                # (3,5)
# will return total elements in matrix (here 15)
si = a.size 

# to transpose a matrix
ww=a.T # transposed to 5x3 matrix

print(a,"\n\n",dim,"\n\n",si,"\n\n",ww,"\n")