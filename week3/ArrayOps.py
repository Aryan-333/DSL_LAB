import numpy as np

list=[6,45,20,19,11,34,28,21]
tuple=(1,2,3,4,5,6,7,8)

A=np.array(list)
print("A = ",A)

B=np.array(tuple).reshape((2,4))
print("B = ",B)

C=np.zeros((3,4))
print("C = ",C)

D=np.arange(0,20,5)
print("D = ",D)

E=C.reshape(2,2,3)
print("E = ",E)

A=A.reshape((2,4))
print("\n",A,"\n")
print("Row wise max elements : ",A.max(axis=1))
print("Column wise max elements : ",A.max(axis=0))
print("Sum of all elements : ",A.sum())