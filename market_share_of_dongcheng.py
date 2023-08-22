import pandas as pd


df1=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/东呈存量酒店-品牌-省份.xlsx')
df2=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/东呈已经部署机器人的酒店-品牌-省份.xlsx')
print(df1.head(10))
print(df2.head(20))


df1_merge_brand_province=df1['品牌名称']+df1['省']
print(df1_merge_brand_province.head(20))

df2_merge_brand_province=df2['品牌名称']+df2['省']
print(df2_merge_brand_province.tail(30))
df1.insert(2,'品牌名称+省',df1_merge_brand_province)
df2.insert(2,'品牌名称+省',df2_merge_brand_province)
print(df1.head(20))
print(df2.head(30))

df_merge=pd.merge(df1,df2,on="品牌名称+省",how='left')

# df_merge=pd.merge(left=df1,right=df2,left_on="品牌名称+省",right_on='品牌名称+省')


print(df_merge.head(30))

market_share=df_merge['CRM客户名称']/df_merge['客户名称']
print(market_share.head(30))

df_merge.insert(7,'云迹占有率',market_share)
df_merge['云迹占有率'].fillna(value=0,inplace=True)
df_merge.rename(columns={'客户名称':'存量酒店（正在运营）的数量','CRM客户名称':'已经上线云迹机器人的酒店数量'},inplace=True)

df_merge.to_excel('/Users/yangzi/Downloads/东呈存量酒店占有率(存量客户在左关联上线机器人的酒店名单).xlsx')
