import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
print(matplotlib.matplotlib_fname())


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV文件
df = pd.read_excel('/Users/yangzi/Desktop/客户列表.xlsx')

print(df.head(10))

# 计算省份、星级、分类的数量和占比
province_counts = df['省份'].value_counts()
star_counts = df['星级'].value_counts()
category_counts = df['分类'].value_counts()

province_ratio = df['省份'].value_counts(normalize=True)
star_ratio = df['星级'].value_counts(normalize=True)
category_ratio = df['分类'].value_counts(normalize=True)

# 定义一个函数，绘制带数量和占比的柱状图
def plot_counts_and_ratio(counts, ratio, title):
    fig, ax = plt.subplots()
    counts.plot(kind='bar', ax=ax, color='skyblue', alpha=0.7)
    ax2 = ax.twinx()
    ax2.plot(ax.get_xticks(), ratio.values, linestyle='-', color='r', alpha=0.5, linewidth=2.5)
    ax.set_ylabel('Counts')
    ax2.set_ylabel('Ratio')
    ax.set_title(title)
    rects = ax.patches
    labels = [f'count: {counts[i]}\nratio: {ratio[i]*100:.2f}%' for i in range(len(rects))]
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, label,
                ha='center', va='bottom')
    plt.show()

# 绘制省份、星级、分类的柱状图
plot_counts_and_ratio(province_counts, province_ratio, '省份分布')
plot_counts_and_ratio(star_counts, star_ratio, '星级分布')
plot_counts_and_ratio(category_counts, category_ratio, '分类分布')
