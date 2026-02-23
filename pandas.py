#intro to pandas
import pandas as pd
import numpy as np

s=pd.Series([1,3,5,7,9])
print(s)

#create a dataframe
data={'Name':['Alice','Bob','Charlie','David','Eve'],
        'Age':[25,30,35,40,45],
        'Marks':[85,90,95,80,75],
        'City':['New York','Los Angeles','Chicago','Houston','Phoenix']}
df=pd.DataFrame(data)
print(df)

print(df.shape) 
print(df.size)
print(df.columns)
print(df.dtypes)

print(df['Name'])
df["blood group"]=["A","B","AB","O","A"]
print(df)

def grade(marks):
    if marks>90:
        return "Distinction"
    elif marks>80:
        return "First Class"
    elif marks>70:
        return "Second Class"
    elif marks>60:
        return "Third Class"
    else:
        return "Fail"
df["Grade"]=df["Marks"].apply(grade)
print(df)

df.loc[0,"City"]="San Francisco"
print(df)

mean1=df["Marks"].mean()
min1=df["Marks"].min()
max1=df["Marks"].max()
sum1=df["Marks"].sum()
print(mean1,min1,max1,sum1)

print(df[df["Marks"]>80])
df1=pd.DataFrame({'c1':[1,2,np.nan],'c2':[4,np.nan,np.nan],'c3':[7,8,9]})
print(df1)
print(df1.isna())
print(df1.dropna())
print(df1.fillna(0))
