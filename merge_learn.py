import pandas
import pandas as pd

df1=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/A抽样的结果-测试.xlsx')
df2=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/B抽样的结果-测试.xlsx')
print(df1.head(10))
print(df2.head(10))

#
# df_merge=pd.merge(left=df1,right=df2,left_on="客户名称",right_on='客户名称')
# print('合并的结果是')
# print(df_merge.head(30))
# print(df_merge.info())
#
print('看看效果,Left合并')
df1=df1.merge(df2,on='客户名称',how='left')
print(df1.head(100))
print(df1.info())



