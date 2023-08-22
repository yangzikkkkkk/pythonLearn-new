import pandas as pd

# 读取Excel文件
df = pd.read_excel('/Users/yangzi/Downloads/发过货的五星级酒店名单CRM.xlsx')

# 删除重复项，保留第一行
df.drop_duplicates(subset='终端客户', keep='first', inplace=True)

# 保存处理后的数据回Excel文件
df.to_excel('/Users/yangzi/Downloads/发过货的五星级酒店名单CRM-2.xlsx', index=False)
