import pandas as pd
df0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/近90天内日均任务大于等于42且只有1台机器人的酒店名单和画像分析 (1).xlsx')
print(df0.head())
print(df0.info())
df1=pd.read_excel('/Users/yangzi/Downloads/近三个月有维修工单的客户.xlsx')
df1.rename(columns={'维修工单-终端客户名称':'CRM客户名称'},inplace=True)
print(df1.head())
print(df1.info())
df0_1=pd.merge(df0,df1,on='CRM客户名称',how='left')
# print(df0_1)
df0_1.drop(columns='记录数_x',inplace=True)
df0_1.drop(columns='记录数_y',inplace=True)
# print(df0_1)
df0_1['维修工单个数'].fillna(value=0,inplace=True)
print(df0_1)










# df0_1.to_excel('/Users/yangzi/Downloads/测试测试.xlsx')








