

print("lalallallal")

import pandas as pd

s1=pd.Series(['a','b','c','d'])
print(s1)

s2=pd.Series(['a','b','c','d'],index=[1,2,3,4])
print(s2)

s3=pd.Series({1:'a',2:'b',3:'c',4:'d'})
print(s3)

print(s1.index)
print(s2.index)
print(s3.index)

df1=pd.DataFrame(['a','b','c','d'])
print(df1)





from datetime import datetime

print(datetime.now())
