import pandas as pd
import matplotlib.pyplot as plt



plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


# 从Excel文件读取数据
df = pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/22 UP预售工作/97 国内酒店清单名单/已经发货的五星级酒店/发过货的五星级酒店名单CRM.xlsx')


# 统计"终端客户-省"的数量和占比
province_counts = df['终端客户-省'].value_counts()
province_counts_top15 = province_counts[:15]  # 只选择前15个数量最多的数据
province_percentages = province_counts_top15 / province_counts_top15.sum()

# 统计"终端客户-市"的数量和占比
city_counts = df['终端客户-市'].value_counts()
city_counts_top15 = city_counts[:15]  # 只选择前15个数量最多的数据
city_percentages = city_counts_top15 / city_counts_top15.sum()

# 统计集团的数量和占比
group_counts = df['集团'].value_counts()
group_counts_top15 = group_counts[:15]  # 只选择前15个数量最多的数据
group_percentages = group_counts_top15 / group_counts_top15.sum()

# 统计品牌名称的数量和占比
brand_counts = df['品牌名称'].value_counts()
brand_counts_top15 = brand_counts[:15]  # 只选择前15个数量最多的数据
brand_percentages = brand_counts_top15 / brand_counts_top15.sum()

# 创建一个2x2的子图
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# 绘制"终端客户-省"的柱状图
axes[0, 0].bar(province_counts_top15.index, province_counts_top15.values)
axes[0, 0].set_xlabel('终端客户-省')
axes[0, 0].set_ylabel('数量')
axes[0, 0].set_title('终端客户-省分布')
axes[0, 0].tick_params(axis='x', rotation=45)
# 添加数量和占比标签
for i, count in enumerate(province_counts_top15.values):
    percentage = province_percentages[i]
    axes[0, 0].text(i, count, f'{count}\n{percentage:.2%}', ha='center', va='bottom')

# 绘制"终端客户-市"的柱状图
axes[0, 1].bar(city_counts_top15.index, city_counts_top15.values)
axes[0, 1].set_xlabel('终端客户-市')
axes[0, 1].set_ylabel('数量')
axes[0, 1].set_title('终端客户-市分布')
axes[0, 1].tick_params(axis='x', rotation=45)
# 添加数量和占比标签
for i, count in enumerate(city_counts_top15.values):
    percentage = city_percentages[i]
    axes[0, 1].text(i, count, f'{count}\n{percentage:.2%}', ha='center', va='bottom')

# 绘制集团的柱状图
axes[1, 0].bar(group_counts_top15.index, group_counts_top15.values)
axes[1, 0].set_xlabel('集团')
axes[1, 0].set_ylabel('数量')
axes[1, 0].set_title('集团分布')
axes[1, 0].tick_params(axis='x', rotation=45)
# 添加数量和占比标签
for i, count in enumerate(group_counts_top15.values):
    percentage = group_percentages[i]
    axes[1, 0].text(i, count, f'{count}\n{percentage:.2%}', ha='center', va='bottom')

# 绘制品牌名称的柱状图
axes[1, 1].bar(brand_counts_top15.index, brand_counts_top15.values)
axes[1, 1].set_xlabel('品牌名称')
axes[1, 1].set_ylabel('数量')
axes[1, 1].set_title('品牌名称分布')
axes[1, 1].tick_params(axis='x', rotation=45)
# 添加数量和占比标签
for i, count in enumerate(brand_counts_top15.values):
    percentage = brand_percentages[i]
    axes[1, 1].text(i, count, f'{count}\n{percentage:.2%}', ha='center', va='bottom')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()
