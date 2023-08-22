import pandas as pd

df0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/（动态3个月）计算客户流失率情况-发货的客户和退机的客户.xlsx',sheet_name='退机明细')
df1=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/（动态3个月）计算客户流失率情况-发货的客户和退机的客户.xlsx',sheet_name='销售发货业务明细')
df0.drop([len(df0)-1],inplace=True)
df1.drop([len(df1)-1],inplace=True)
# print(df0.tail(20))
# print(df1.tail(20))

print(df0.info())
print(df1.info())

df0_hotel_product_merge=df0['客户名称']+df0['产品归属（机器人/货柜）']
print(df0_hotel_product_merge)
df1_hotel_product_merge=df1['客户名称']+df1['产品归属（机器人/货柜）']
print(df1_hotel_product_merge)

df0.insert(2,'客户名称+产品归属',df0_hotel_product_merge)
df1.insert(2,'客户名称+产品归属',df1_hotel_product_merge)

# print(df0.head())
# print(df1.head())

print('在这段时间内，销售发货业务的单据对应的客户数是')
print(df1['客户名称'].describe())
print('在这段时间内，退机的单据对应的客户数是')
print(df0['客户名称'].describe())

merged_df0_df1=pd.merge(df1,df0,on='客户名称+产品归属',how='left')
print('来看下，合并以后的结果是什么呢,要把空置填写为0')
merged_df0_df1['逻辑处理单据数量_y'].fillna(value=0,inplace=True)
# print(merged_df0_df1.head(10))

sum=merged_df0_df1['逻辑处理单据数量_x']+merged_df0_df1['逻辑处理单据数量_y']
merged_df0_df1.insert(21,'合并数量',sum)

print('看看  合并数量 剔除掉是0的结果')
merged_sum=merged_df0_df1[merged_df0_df1['合并数量'] !=0]
# print(merged_sum.head(20))
# print(merged_sum.columns)

print('这段时间内，退机后，还留存的客户数量是')
print(merged_sum['客户名称_x'].describe())
# print(merged_sum.head(1000))
merged_df0_df1.to_excel('/Users/yangzi/Downloads/计算测试.xlsx')


