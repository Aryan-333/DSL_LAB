import random
a = random.choice([1,2,3,4,5]) #this will pick one number from the list randomly
b= random.choice('python') #will pick one character from the string randomly
c = random.randrange(25,50) #will pick one integer between 25 to 50
d = random.randrange(25,50,2) #will pick one integer between 25 to 50 with step size of 2
e= random.random() #will pick a random number between 0 to 1
f = random.uniform(5,10) #will pick a floating point number between 5 to 10
g = random.shuffle([1,2,3,4,5]) #will shuffle the list elements
h =random.seed(10) #to get same random value during every execution

print(a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g,"\n",h,"\n\n")