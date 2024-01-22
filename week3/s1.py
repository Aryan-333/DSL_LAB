import numpy as np

# data type checking
A = np.array ([2,5,10])
print(A.dtype)

#Creating sequence of sequence will create 2-dimensional array.
A=np.array([(3,4,5),(12,6,1)])
Z=np.zeros((2,4)) # will create zero matrix of dimension 2x4
B=np.ones((3,3)) # will create one’s matrix of dimension 3x3

print(A,"\n\n",Z,"\n\n",B,"\n")

#To create a sequence of data,
S=np.arange(10,30,5)
print(S) #will give (10,15,20,25,30), with step size of 5
P=np.arange( 0, 2, 0.3 ) # it accepts float arguments
print("\n\n",P)


#Instead of step-size, we can specify total number of elements in the array using
S1=np.linspace(0,2,9) # produce 9 numbers starting 0 & ends with 2array([ 0. , 0.25, 0.5 , 0.75, 1. , 1.25, 1.5 , 1.75, 2. ])
print("\n\n",S1)
