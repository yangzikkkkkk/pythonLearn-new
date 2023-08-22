import pandas as pd

df1=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/已交付机器人酒店客房数大于等于100的名单.xlsx')
df2=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/近90天内日均任务大于等于30的酒店名单和画像分析.xlsx')

print(df1.info())
print(df2.info())


df1_hotel_and_group=df1[['地点名称','全局可引用-集团名称','集团分类结果']]
df2_hotel_and_group=df2[['地点名称','全局可引用-集团名称','集团分类结果']]

print(df1_hotel_and_group.head(20))
print(df2_hotel_and_group.tail(30))

#
#
# d3=df1_hotel_and_group.merge(df2_hotel_and_group,on='地点名称',how='outer')
# print(d3)


#
df3=[df1_hotel_and_group,df2_hotel_and_group]
df3_show=pd.concat(df3)
print(df3_show)
df3_show.drop_duplicates(subset='地点名称',keep='last',inplace=True)
print(df3_show)
df3_show.to_excel('/Users/yangzi/Downloads/房间数大于100或者近90天日均任务大于等于30的酒店名单.xlsx')


# df3=df1_hotel_and_group.append(df2_hotel_and_group)
# df3.index(0:10000,step=1)

# print(df3.index)


# print(df3.info())
# print(df3)

# df3.to_excel('/Users/yangzi/Downloads/测试.xlsx')