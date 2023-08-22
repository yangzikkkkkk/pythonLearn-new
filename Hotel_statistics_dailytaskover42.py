import pandas as pd

df0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/近90天内日均任务大于等于42且只有1台机器人的酒店名单和画像分析 (1).xlsx')
print(df0.head())
print(df0.info())


print(df0['全局可引用-集团名称'].unique())


eight_group=['锦江','华住','首旅如家','亚朵','开元','尚美','格林','东呈国际']

df0_8group=df0[df0['全局可引用-集团名称'].isin(eight_group)]

print(df0_8group)
df0_8group_clear=df0_8group[['地点名称','全局可引用-集团名称','品牌名称','省']]

# df0_8group_clear.to_excel('/Users/yangzi/Downloads/ceshiceshi.xlsx')

grouped=df0_8group_clear.groupby(['全局可引用-集团名称', '品牌名称','省'])
result = grouped.count()
print(result)




result.to_excel('/Users/yangzi/Downloads/近90天内日均任务大于等于42且只有1台机器人的酒店名单和画像分析-汇总统计-集团品牌省.xlsx')

#
# print(df0['全局可引用-集团名称'].unique())
# df_huazhu=df0[df0['全局可引用-集团名称']=='华住']
# print(df_huazhu.head())
# print(df_huazhu['地点名称'].count())

# for brand in df_huazhu['品牌名称'].unique():
#     print(brand)
#     df_huazhu_brand=df_huazhu[df_huazhu['品牌名称']==brand]
#     print(df_huazhu_brand['地点名称'].count())


#
# groupnames=['锦江','华住','首旅如家','亚朵','尚美','格林','开元','东呈国际',]
# for name in groupnames:
#     print(name)
#     df_group=df0[df0['全局可引用-集团名称']==name]
#     # print('酒店的数量是')
#     print(df_group['地点名称'].count())
#     for brand in df_group['品牌名称'].unique():
#         print(name+brand)
#         df_group_brand=df_group[df_group['品牌名称']==brand]
#         print(df_group_brand['地点名称'].count())
#         for province in df_group_brand['省'].unique():
#             print(name+brand+province)
#             df_group_brand_province=df_group_brand[df_group_brand['省']==province]
#             print(df_group_brand_province['地点名称'].count())
#









