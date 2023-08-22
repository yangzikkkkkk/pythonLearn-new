import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 然后绘制图表

# 导入Excel数据
data = pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/22 UP预售工作/102 国内酒店清单名单和CRM上已经发货的酒店名单/五星级酒店-携程上的名单-分析图/五星级酒店-携程上的名单.xlsx')




# 分析酒店的省、城市、类型、房间数分组、品牌、集团和酒店性质的分布情况
province_counts = data['省份'].value_counts().nlargest(15)
city_counts = data['城市'].value_counts().nlargest(15)
type_counts = data['类型'].value_counts().nlargest(15)
room_group_counts = data['房间数分组'].value_counts().nlargest(15)
brand_counts = data['品牌'].value_counts().nlargest(15)
group_counts = data['集团'].value_counts().nlargest(15)
property_counts = data['酒店性质'].value_counts().nlargest(15)

# 设置子图布局
fig, axes = plt.subplots(2, 1, figsize=(12, 18))

# 绘制省份分布柱状图
axes[0].bar(province_counts.index, province_counts.values)
axes[0].set_title('Province Distribution')
axes[0].set_xlabel('Province')
axes[0].set_ylabel('Count')
axes[0].set_xticklabels(province_counts.index, rotation='vertical')
for i, v in enumerate(province_counts):
    axes[0].text(i, v, str(v), ha='center', va='bottom')
    axes[0].text(i, v / sum(province_counts), f'{(v / sum(province_counts)):.2%}', ha='center', va='top')

# 绘制城市分布柱状图
axes[1].bar(city_counts.index, city_counts.values)
axes[1].set_title('City Distribution')
axes[1].set_xlabel('City')
axes[1].set_ylabel('Count')
axes[1].set_xticklabels(city_counts.index, rotation='vertical')
for i, v in enumerate(city_counts):
    axes[1].text(i, v, str(v), ha='center', va='bottom')
    axes[1].text(i, v / sum(city_counts), f'{(v / sum(city_counts)):.2%}', ha='center', va='top')

plt.tight_layout()
plt.show()

# 设置子图布局
fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# 绘制类型分布柱状图
axes[0, 0].bar(type_counts.index, type_counts.values)
axes[0, 0].set_title('Type Distribution')
axes[0, 0].set_xlabel('Type')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_xticklabels(type_counts.index, rotation='vertical')
for i, v in enumerate(type_counts):
    axes[0, 0].text(i, v, str(v), ha='center', va='bottom')
    axes[0, 0].text(i, v / sum(type_counts), f'{(v / sum(type_counts)):.2%}', ha='center', va='top')

# 绘制房间数分组分布柱状图
axes[0, 1].bar(room_group_counts.index, room_group_counts.values)
axes[0, 1].set_title('Room Group Distribution')
axes[0, 1].set_xlabel('Room Group')
axes[0, 1].set_ylabel('Count')
axes[0, 1].set_xticklabels(room_group_counts.index, rotation='vertical')
for i, v in enumerate(room_group_counts):
    axes[0, 1].text(i, v, str(v), ha='center', va='bottom')
    axes[0, 1].text(i, v / sum(room_group_counts), f'{(v / sum(room_group_counts)):.2%}', ha='center', va='top')

# 绘制品牌分布柱状图
axes[1, 0].bar(brand_counts.index, brand_counts.values)
axes[1, 0].set_title('Brand Distribution')
axes[1, 0].set_xlabel('Brand')
axes[1, 0].set_ylabel('Count')
axes[1, 0].set_xticklabels(brand_counts.index, rotation='vertical')
for i, v in enumerate(brand_counts):
    axes[1, 0].text(i, v, str(v), ha='center', va='bottom')
    axes[1, 0].text(i, v / sum(brand_counts), f'{(v / sum(brand_counts)):.2%}', ha='center', va='top')

# 绘制集团分布柱状图
axes[1, 1].bar(group_counts.index, group_counts.values)
axes[1, 1].set_title('Group Distribution')
axes[1, 1].set_xlabel('Group')
axes[1, 1].set_ylabel('Count')
axes[1, 1].set_xticklabels(group_counts.index, rotation='vertical')
for i, v in enumerate(group_counts):
    axes[1, 1].text(i, v, str(v), ha='center', va='bottom')
    axes[1, 1].text(i, v / sum(group_counts), f'{(v / sum(group_counts)):.2%}', ha='center', va='top')

plt.tight_layout()
plt.show()
