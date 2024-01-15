import pandas as pd
d1={"Name":['a','b','c','d','e']}

d2={"mat":[80.0,90.0,77.5,87.5,86.5],"phy":[80.0,90.0,77.5,87.5,86.5],"chem":[80.0,90.0,77.5,87.5,86.5],"Bio":[80.0,90.0,77.5,87.5,86.5]}
df1=pd.DataFrame(d1,columns=d1.keys())
df2=pd.DataFrame(d2,columns=d2.keys())
df_final=pd.concat([df1,df2],axis=1)
df_final['final']=df_final['mat']+df_final['phy']+df_final['chem']+df_final['Bio']
print(df_final)