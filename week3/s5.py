import numpy as np
#Array operations
a = np.array( [20,30,40,50] )
b = np.arange( 4 )

#array([0, 1, 2, 3])

c = a-b
# array([20, 29, 38, 47])

d = b**2
# array([0, 1, 4, 9])

e= 10*np.sin(a)
#array([ 9.12945251, −9.88031624, 7.4511316 , −2.62374854])
f=a<35
# array([ True, True, False, False], dtype=bool)

print(b,"\n\n",c,"\n\n",d,"\n\n",e,"\n",f)
