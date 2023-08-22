import pandas as pd

df1=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/近90天内日均任务大于等于42且只有1台机器人的酒店名单和画像分析 (1).xlsx')
df2=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/交付超过2.5年（动态）以上的酒店名单.xlsx')

df1.drop([len(df1)-1],inplace=True)
df2.drop([len(df2)-1],inplace=True)

print(df1.info())
print(df2.info())


print(df1.tail())
print(df2.tail())





df1_hotel_and_group=df1[['地点名称','全局可引用-集团名称','集团分类结果','该门店有几台机器人']]
df2_hotel_and_group=df2[['地点名称','全局可引用-集团名称','集团分类结果','该门店有几台机器人']]

print(df1_hotel_and_group.head(20))
print(df2_hotel_and_group.tail(30))

print(df1_hotel_and_group.info())
print(df2_hotel_and_group.info())





# #
# #
# # d3=df1_hotel_and_group.merge(df2_hotel_and_group,on='地点名称',how='outer')
# # print(d3)





df3=[df1_hotel_and_group,df2_hotel_and_group]
df3_show=pd.concat(df3)
print(df3_show)
df3_show.drop_duplicates(subset='地点名称',keep='last',inplace=True)
print(df3_show)
df3_show.to_excel('/Users/yangzi/Downloads/交付时间超过2.5年（动态）或者近90天日均任务大于等于42次的酒店名单.xlsx')
print(df3_show.info())

# df3=df1_hotel_and_group.append(df2_hotel_and_group)
# df3.index(0:10000,step=1)

# print(df3.index)


# print(df3.info())
# print(df3)

# df3.to_excel('/Users/yangzi/Downloads/测试.xlsx')