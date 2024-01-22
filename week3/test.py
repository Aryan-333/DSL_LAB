import numpy as np
import random

A = np.array ([(1,2,3,4,5),(6,7,8,9,10)])
print(A)
print(A.dtype)

print(random.random()*5)
print(random.choice("Hello World"))
print(random.randrange(0,50))

B = np.array([[1,1],[0,1]])
C = np.array([[2,0],[3,4]])

print("\n",B)
print("\n",C)
print("\n",np.dot(B,C))

print(A[:,2:5])

A1=np.array([(3,4,5),(12,6,1)])
A2=np.array([(1,2,6),(-4,3,8)])
print("\n",A1,"\n\n",A2)
D1=np.vstack((A1,A2))
D2=np.hstack((A1,A2))
print("\n",D1,"\n\n",D2)