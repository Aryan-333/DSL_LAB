import numpy as np

# 3- Dimensional array
c = np.arange(24).reshape(2,3,4) # 1st value indicates (no of planes) (3,4) is the dimension
                    # [[[ 0 1 2 3]
                    # [ 4 5 6 7]
                    # [ 8 9 10 11]]
                    # [[12 13 14 15]
                    # [16 17 18 19]
                    # [20 21 22 23]]]
b=c.shape #will return (2,3,4)
d=c[1,...] #is equal to c[1,:,:] # will fetch all elements of 2nd plane
e=c[...,2] #is equal to c[:,:,2] [[3,7,11],[15,19,23]]

print(c,"\n\n",b,"\n\n",d,"\n\n",e,"\n")
