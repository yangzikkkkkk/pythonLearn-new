import pandas as pd

# 读取两个Excel文件
df1 = pd.read_excel('/Users/yangzi/Downloads/左表.xlsx')
df2 = pd.read_excel('/Users/yangzi/Downloads/庭锐需求找设备ID.xlsx')

# 使用merge方法进行合并，参数on是你想要依据合并的列
merged_df = pd.merge(df2, df1, on='storeid')

# 将合并后的数据保存到新的Excel文件中
merged_df.to_excel('/Users/yangzi/Downloads/总表.xlsx', index=False)
