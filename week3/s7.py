import numpy as np
# Indexing, Slicing & Iterating Array
a = np.arange(10)**3

# array([ 0, 1, 8, 27, 64, 125, 216, 343, 512, 729])
c= a[2:5]
#array([ 8, 27, 64])
d = a[0:6:2]
# array([0,8,64,216])
# Let ‘b’, is an input matrix of size 5x4
b=np.array ([[ 0, 1, 2, 3],
[10, 11, 12, 13],
[20, 21, 22, 23],
[30, 31, 32, 33],
[40, 41, 42, 43]])

e =b[2,3] #will fetch 23
f =b[0:5,1] #or b[:5,1] or b[:,1] #will fetch [1,11,21,31,41]
g =b[-1,:] # will fetch last row
h = b[:,-1] # will fetch last col

for row in b:
    print(row) # will print every row
for element in b.flat:
    print (element) # will show all elements of b in 1−D array

print(a,"\n\n",c,"\n\n",d,"\n\n",e,"\n\n",f,"\n\n",g,"\n\n",h,"\n\n")