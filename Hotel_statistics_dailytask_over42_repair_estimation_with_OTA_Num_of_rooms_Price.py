import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([5, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6])
y = np.array([0.98, 0.92, 0.88, 0.85, 0.8, 0.78,0.75, 0.71, 0.69, 0.66, 0.62, 0.6, 0.57, 0.54, 0.5 ])

plt.figure(num="OTA和入住率的关系预测")
plt.scatter(x,y)
# plt.show()

model = LinearRegression()
model.fit(x.reshape(-1,1), y)
# y_pred = model.predict([[5]])

# 计算 R2 值
r2 = model.score(x.reshape(-1,1), y)
print('R2 值：', r2)
# print(y_pred)



df0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/近90天内日均任务大于等于42且只有1台机器人的酒店名单和画像分析 (1).xlsx')
print(df0.head())
print(df0.info())
df1=pd.read_excel('/Users/yangzi/Downloads/近三个月有维修工单的客户.xlsx')
df1.rename(columns={'维修工单-终端客户名称':'CRM客户名称'},inplace=True)
print(df1.head())
print(df1.info())
df0_1=pd.merge(df0,df1,on='CRM客户名称',how='left')
# print(df0_1)
df0_1.drop(columns='记录数_x',inplace=True)
df0_1.drop(columns='记录数_y',inplace=True)
# print(df0_1)
df0_1['维修工单个数'].fillna(value=0,inplace=True)
print(df0_1)
df2=pd.read_excel('/Users/yangzi/Downloads/（总体价格非空）客户带出房间数-OTA-价格区间.xlsx')
df2.rename(columns={'客户名称':'CRM客户名称'},inplace=True)
# print(df2.info())
# print(df2.head())

df0_1_2=pd.merge(df0_1,df2,on='CRM客户名称',how='left')

df0_1_2['价格区间'].replace('350-400元','375',inplace=True)
df0_1_2['价格区间'].replace('150-200元','175',inplace=True)
df0_1_2['价格区间'].replace('500-550元','525',inplace=True)
df0_1_2['价格区间'].replace('800元以上','1000',inplace=True)
df0_1_2['价格区间'].replace('550-600元','575',inplace=True)
df0_1_2['价格区间'].replace('250-300元','275',inplace=True)
df0_1_2['价格区间'].replace('400-450元','425',inplace=True)
df0_1_2['价格区间'].replace('300-350元','325',inplace=True)
df0_1_2['价格区间'].replace('450-500元','475',inplace=True)
df0_1_2['价格区间'].replace('100-150元','125',inplace=True)
df0_1_2['价格区间'].replace('750-800元','775',inplace=True)
df0_1_2['价格区间'].replace('600-650元','625',inplace=True)
df0_1_2['价格区间'].replace('200-250元','225',inplace=True)
df0_1_2['价格区间'].replace('100元以下','80',inplace=True)
df0_1_2['价格区间'].replace('700-750元','725',inplace=True)
df0_1_2['价格区间'].replace('650-700元','675',inplace=True)
df0_1_2.rename(columns={'价格区间':'根据价格区间预估数'},inplace=True)
df0_1_2[['根据价格区间预估数']]=df0_1_2[['根据价格区间预估数']].astype(float)
print(df0_1_2.head())
print(df0_1_2.info())
average_OTA=df0_1_2['酒店OTA得分'].mean()
df0_1_2['酒店OTA得分'].fillna(value=average_OTA, inplace=True)
estimate_Occupy_rate= model.predict(df0_1_2[['酒店OTA得分']])
print('看看预计的入住率是多少')
print(estimate_Occupy_rate)
df0_1_2.insert(13,'根据OTA得分预估的入住率',estimate_Occupy_rate)


estimateScore=df0_1_2['根据价格区间预估数']*df0_1_2['房间数_y']*df0_1_2['根据OTA得分预估的入住率']
print(estimateScore)
df0_1_2.insert(14,'估计分数=价格估计*房间数*根据OTA得分预估的入住率',estimateScore)
df0_1_2['估计分数=价格估计*房间数*根据OTA得分预估的入住率'].fillna(value=estimateScore.mean(),inplace=True)
median_of_recent90days_hotel=26747.5
over_median_or_not=df0_1_2['估计分数=价格估计*房间数*根据OTA得分预估的入住率']>median_of_recent90days_hotel
print(over_median_or_not)
df0_1_2.insert(15,'判断分值是否大于近90天客户成交中位数26747高于为TRUE',over_median_or_not)

# df0_1_2.to_excel('/Users/yangzi/Downloads/近90天内日均任务大于等于42且只有1台机器人的酒店名单带出90天内是否有维修和购买力评估.xlsx')

df3=pd.read_excel('/Users/yangzi/Downloads/（估计送一次外卖往返时间）酒店机器人单次送物任务时长统计.xlsx')
print(df3.head())
print(df3.info())
df0_1_2_3=pd.merge(df0_1_2,df3,on='地点名称',how='left')
df0_1_2_3.drop([len(df0_1_2_3)-1],inplace=True)
print(df0_1_2_3.tail(10))
print(df0_1_2_3.columns)

Food_delivery_estimated=df0_1_2_3['房间数_x']*0.45
# Food_delivery_estimated=Food_delivery_estimated.astype(int)
print(Food_delivery_estimated)
Food_delivery_estimated_during18_20_2hours=Food_delivery_estimated*0.3
print(Food_delivery_estimated_during18_20_2hours)
print(Food_delivery_estimated_during18_20_2hours.describe())



Food_delivery_estimated_during18_20_2hours.fillna(value=0,inplace=True)
Food_delivery_estimated_during18_20_2hours_int=Food_delivery_estimated_during18_20_2hours.astype(int)
print(Food_delivery_estimated_during18_20_2hours_int.describe())
df0_1_2_3.insert(23,'全天的外卖估计数量房间数乘以0点45',Food_delivery_estimated)
df0_1_2_3.insert(24,'发生在18-20点的外卖预估数量',Food_delivery_estimated_during18_20_2hours_int)
print(df0_1_2_3.tail())
print(df0_1_2_3.info())


Food_have_to_waite_time_s=(df0_1_2_3['预估的送外卖时长（送物往返+11秒取）单位秒']-120*60/df0_1_2_3['发生在18-20点的外卖预估数量'])*(df0_1_2_3['发生在18-20点的外卖预估数量']-1)/2
Food_have_to_waite_time_m=Food_have_to_waite_time_s/60
Food_have_to_waite_time_m.loc[Food_have_to_waite_time_m<0]=np.nan
# Food_have_to_waite_time_m.loc[Food_have_to_waite_time_m==0]=np.nan
# my_series.loc[my_series < 0] = np.nan
print(Food_have_to_waite_time_m)

Consumer_have_to_waite_for_his_food_s=Food_have_to_waite_time_s+df0_1_2_3['平均送物时长（秒）']
Consumer_have_to_waite_for_his_food_m=Consumer_have_to_waite_for_his_food_s/60

Consumer_have_to_waite_for_his_food_m.loc[Consumer_have_to_waite_for_his_food_m<0]=np.nan
print(Consumer_have_to_waite_for_his_food_m)

df0_1_2_3.insert(25,'发生在18-20点的外卖平均需要等待被机器人送的时间单位分钟',Food_have_to_waite_time_m)
# df0_1_2_3.loc[df0_1_2_3['发生在18-20点的外卖平均需要等待被机器人送的时间单位分钟'] < 0, '发生在18-20点的外卖平均需要等待被机器人送的时间单位分钟'] = np.nan
df0_1_2_3.insert(26,'发生在18-20点的外卖平均住客需要等待的时间单位分钟',Consumer_have_to_waite_for_his_food_m)

Consumer_have_to_waite_for_his_food_m_test=Consumer_havem_to_waite_for_his_food_m.fillna(value=0)
Consumer_have_to_waite_for_his_food_m_test.replace(np.inf,0,inplace=True)
print(Consumer_have_to_waite_for_his_food_m_test)



skewness = skew(Consumer_have_to_waite_for_his_food_m_test)
print("偏度:", skewness)
# 计算峰度
kurt = kurtosis(Consumer_have_to_waite_for_his_food_m_test)
print("峰度:", kurt)


# Consumer_have_to_waite_for_his_food_m
a=pd.cut(Consumer_have_to_waite_for_his_food_m,[5,10,14,20,30,60,120,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'时间区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(num='看看住客等待时间，换算成分钟，大概的分布是什么，排除掉空值')
ax=sns.barplot(x="时间区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.8, p.get_height(), ha="center")
plt.show()

# df0_1_2_3.to_excel('/Users/yangzi/Downloads/近90天内日均任务大于等于42且只有1台机器人的酒店名单带出90天内是否有维修和购买力评估+预计外卖等待时间估计.xlsx')