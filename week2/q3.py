import pandas as pd

d1={"Name":["Aryan","Abel","daniel"],"Height":7.5,"Qualification":"bt",34:23}
print(d1["Name"][0])
print(d1.keys())
df = pd.DataFrame(d1,columns=d1.keys())
print(df)
print("\n")

d2=["moksha","anurag","priyanshu"]
df["address"]=d2
print(df)


