import pandas as pd

# Create two data frames
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 4]})

df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value': [5, 6, 7, 8]})

# Inner join
inner_merged_df = pd.merge(df1, df2, on='key', how='inner')
print('Inner join:')
print(inner_merged_df)

# Outer join
outer_merged_df = pd.merge(df1, df2, on='key', how='outer')
print('Outer join:')
print(outer_merged_df)

# Left join
left_merged_df = pd.merge(df1, df2, on='key', how='left')
print('Left join:')
print(left_merged_df)

# Right join
right_merged_df = pd.merge(df1, df2, on='key', how='right')
print('Right join:')
print(right_merged_df)




from scipy.stats import skew, kurtosis

data = [1, 2, 3, 4, 5]

# 计算偏度
skewness = skew(data)
print("偏度:", skewness)

# 计算峰度
kurt = kurtosis(data)
print("峰度:", kurt)



import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成一个包含10个城市每月平均气温的随机数据集
np.random.seed(0)
data = pd.DataFrame(np.random.rand(12, 10)*30, columns=['City{}'.format(i+1) for i in range(10)],
                    index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# 绘制热力图
sns.heatmap(data, cmap='coolwarm', annot=True, fmt='.1f')
plt.show()

