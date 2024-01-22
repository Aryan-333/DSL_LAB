import numpy as np
# Matrix operations
A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )
b =A*B # elementwise product
            # array([[2, 0],
            # [0, 4]])
c= A.dot(B) # matrix product
            # array([[5, 4],
            # [3, 4]])
# (OR)

d = np.dot(A, B)
# array([[5, 4],
# [3, 4]])

e = np.arange(12).reshape(3,4)
            # array([[ 0, 1, 2, 3],
            # [ 4, 5, 6, 7],
            # [ 8, 9, 10, 11]])
f= e.sum(axis=0)
            # array([12, 15, 18, 21])# sum of each column
g= e.sum(axis=1)
            # array([6, 22, 38])


print(b,"\n\n",c,"\n\n",d,"\n\n",e,"\n\n",f,"\n\n",g)