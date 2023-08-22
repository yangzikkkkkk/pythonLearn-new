import pandas as pd


df0=pd.read_excel('/Users/yangzi/Downloads/UP的任务明细1.xlsx')
df0.drop([len(df0)-1],inplace=True)

print(df0.info())
print(df0.tail(20))

print(df0['任务时长'].describe())