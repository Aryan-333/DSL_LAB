import pandas as pd

d1={"Name":["Aryan","Abel","daniel"],"Height":[7.5,8,9],"Qualification":["bt","bc","bb"],}
df = pd.DataFrame(d1,columns=d1.keys())
print(df)
print("\n")


df.insert(1,"vishal",["vishag","abel","vv"],True)
print(df)


