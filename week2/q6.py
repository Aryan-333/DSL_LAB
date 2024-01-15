import pandas as pd
d1={"Name":['a','b','c','d','e']}
d2={"mat":[80,90,77,875,865],"phy":[800,900,775,875,865],"chem":[800,900,775,875,865],"Bio":[800,900,77,875,865]}
df1=pd.DataFrame(d1,columns=d1.keys())
df2=pd.DataFrame(d2,columns=d2.keys())
df_final=pd.concat([df1,df2],axis=1)
df_final['final']=df_final.loc[0:4,["mat","phy","chem","Bio"]].sum(axis=1)
df_final.loc['Mean']=df_final.mean(numeric_only=True)
print(df_final)