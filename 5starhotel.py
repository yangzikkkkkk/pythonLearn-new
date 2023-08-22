import pandas as pd

# 读取Excel文件
df = pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/22 UP预售工作/102 国内酒店清单名单和CRM上已经发货的酒店名单/五星级酒店-携程上的名单(已自动还原)-实习生手动合并.xlsx')

# 只保留我们感兴趣的列
df = df[['酒店名称', '是否签约', '城市', '集团']]

# 将集团列中的空值替换为"单体"
df['集团'].fillna('单体', inplace=True)

# 计算各城市的酒店数量，并取前15个
top_15_cities = df['城市'].value_counts().nlargest(15)

result = []

# 在这些城市中，计算各城市的酒店是否签约的数量和集团分布
for city in top_15_cities.index:
    city_hotels = df[df['城市'] == city]

    # 签约的酒店数量和集团分布
    signed_hotels = city_hotels[city_hotels['是否签约'] == 1]
    signed_hotels_distribution = signed_hotels['集团'].value_counts()
    for group, count in signed_hotels_distribution.items():
        result.append([city, '签约', group, count])

    # 未签约的酒店数量和集团分布
    unsigned_hotels = city_hotels[city_hotels['是否签约'] == 0]
    unsigned_hotels_distribution = unsigned_hotels['集团'].value_counts()
    for group, count in unsigned_hotels_distribution.items():
        result.append([city, '未签约', group, count])

# 将结果保存为新的DataFrame并输出到Excel
result_df = pd.DataFrame(result, columns=['城市', '签约状态', '集团', '数量'])
result_df.to_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/22 UP预售工作/102 国内酒店清单名单和CRM上已经发货的酒店名单/五星级酒店-携程上的名单(已自动还原)-实习生手动合并22222.xlsx', index=False)
