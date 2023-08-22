
# 导入pandas库
import pandas as pd


# 导入matplotlib库
import matplotlib.pyplot as plt

import matplotlib

matplotlib.rc("font", family="	Arial Unicode MS") # 设置字体为SimHei，也可以选择其他支持中文的字体

# 指定excel文件的路径和名称
file_path = "/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/22 UP预售工作/102 国内酒店清单名单和CRM上已经发货的酒店名单/已经发货的五星级酒店-分析图/发过货的五星级酒店名单CRM.xlsx"

# 指定工作表的名称
sheet_name = "五星级酒店发过货的名单"

# 读取数据
df = pd.read_excel(file_path, sheet_name)



# 对终端客户-省进行统计，并筛选出数量最多的前10个
province_count = df["终端客户-省"].value_counts().nlargest(10)

# 对终端客户-市进行统计，并筛选出数量最多的前10个
city_count = df["终端客户-市"].value_counts().nlargest(10)

# 对集团进行统计，并筛选出数量最多的前10个
group_count = df["集团"].value_counts().nlargest(10)

# 对品牌名称进行统计，并筛选出数量最多的前10个
brand_count = df["品牌名称"].value_counts().nlargest(10)

# 创建一个两行两列的大图
fig, axes = plt.subplots(2, 2, figsize=(20, 12))

# 在第一行第一列的位置绘制终端客户-省的柱状图
axes[0, 0].bar(province_count.index, province_count.values)
axes[0, 0].set_title("酒店按终端客户-省分布情况")
axes[0, 0].set_xlabel("终端客户-省")
axes[0, 0].set_ylabel("酒店数量")
axes[0, 0].set_xticks(province_count.index) # 设置x轴刻度为省份名称
axes[0, 0].tick_params(axis="x", rotation=45) # 设置x轴刻度旋转角度

# 计算总数和占比
total = province_count.sum()
percentages = province_count / total * 100

# 在柱子上方显示数字和占比，保留一位小数，注意把浮点数转换成字符串
for x, y, p in zip(province_count.index, province_count.values, percentages.values):
    axes[0, 0].text(x, y + 5, f"{y} ({float(p):.1f}%)", ha="center", va="bottom")

# 在第一行第二列的位置绘制终端客户-市的柱状图
axes[0, 1].bar(city_count.index, city_count.values)
axes[0, 1].set_title("酒店按终端客户-市分布情况")
axes[0, 1].set_xlabel("终端客户-市")
axes[0, 1].set_ylabel("酒店数量")
axes[0, 1].set_xticks(city_count.index) # 设置x轴刻度为城市名称
axes[0, 1].tick_params(axis="x", rotation=45) # 设置x轴刻度旋转角度

# 计算总数和占比
total = city_count.sum()
percentages = city_count / total * 100

# 在柱子上方显示数字和占比，保留一位小数，注意把浮点数转换成字符串
for x, y, p in zip(city_count.index, city_count.values, percentages.values):
    axes[0, 1].text(x, y + 5, f"{y} ({float(p):.1f}%)", ha="center", va="bottom")

# 在第二行第一列的位置绘制集团的柱状图
axes[1, 0].bar(group_count.index, group_count.values)
axes[1, 0].set_title("酒店按集团分布情况")
axes[1, 0].set_xlabel("集团")
axes[1, 0].set_ylabel("酒店数量")
axes[1, 0].set_xticks(group_count.index) # 设置x轴刻度为集团名称
axes[1, 0].tick_params(axis="x", rotation=45) # 设置x轴刻度旋转角度

# 计算总数和占比
total = group_count.sum()
percentages = group_count / total * 100

# 在柱子右侧显示数字和占比，保留一位小数，注意把浮点数转换成字符串
for x, y, p in zip(group_count.index, group_count.values, percentages.values):
    axes[1, 0].text(x + 0.2, y, f"{y} ({float(p):.1f}%)", ha="left", va="center")





# 在第二行第二列的位置绘制品牌名称的柱状图
axes[1, 1].bar(brand_count.index, brand_count.values)
axes[1, 1].set_title("酒店按品牌名称分布情况")
axes[1, 1].set_xlabel("品牌名称")
axes[1, 1].set_ylabel("酒店数量")
axes[1, 1].set_xticks(brand_count.index) # 设置x轴刻度为品牌名称
axes[1, 1].tick_params(axis="x", rotation=45) # 设置x轴刻度旋转角度

# 计算总数和占比
total = brand_count.sum()
percentages = brand_count / total * 100

# 在柱子右侧显示数字和占比，保留一位小数，注意把浮点数转换成字符串
for x, y, p in zip(brand_count.index, brand_count.values, percentages.values):
    axes[1, 1].text(x + 0.2, y, f"{y} ({float(p):.1f}%)", ha="left", va="center")

plt.show() # 显示大图
