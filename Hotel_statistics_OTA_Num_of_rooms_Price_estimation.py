import pandas as pd

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([5, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6])
y = np.array([0.98, 0.92, 0.88, 0.85, 0.8, 0.78,0.75, 0.71, 0.69, 0.66, 0.62, 0.6, 0.57, 0.54, 0.5 ])

plt.figure(num="OTA和入住率的关系预测")
plt.scatter(x,y)
plt.show()

model = LinearRegression()
model.fit(x.reshape(-1,1), y)
# y_pred = model.predict([[5]])

# 计算 R2 值
r2 = model.score(x.reshape(-1,1), y)
print('R2 值：', r2)
# print(y_pred)




df0=pd.read_excel('/Users/yangzi/Downloads/近90天内销售发货业务明细.xlsx')
print(df0.head())
print(df0.info())
df0_hotel=df0[['客户名称']]
df0_hotel_clear=df0_hotel.dropna()
print(df0_hotel_clear)

# df0_hotel.dropna(inplace=True)
# print(df0_hotel)

df1=pd.read_excel('/Users/yangzi/Downloads/（总体价格非空）客户带出房间数-OTA-价格区间.xlsx')
print(df1.head())
print(df1.info())


df0_1=pd.merge(df0_hotel_clear,df1,on='客户名称',how='left')
df0_1.drop([len(df0_1)-1],inplace=True)
df0_1.dropna(how='any',inplace=True)
print(df0_1)
print(df0_1.info())
print(df0_1['价格区间'].unique())

df0_1['价格区间'].replace('350-400元','375',inplace=True)
df0_1['价格区间'].replace('150-200元','175',inplace=True)
df0_1['价格区间'].replace('500-550元','525',inplace=True)
df0_1['价格区间'].replace('800元以上','1000',inplace=True)
df0_1['价格区间'].replace('550-600元','575',inplace=True)
df0_1['价格区间'].replace('250-300元','275',inplace=True)
df0_1['价格区间'].replace('400-450元','425',inplace=True)
df0_1['价格区间'].replace('300-350元','325',inplace=True)
df0_1['价格区间'].replace('450-500元','475',inplace=True)
df0_1['价格区间'].replace('100-150元','125',inplace=True)
df0_1['价格区间'].replace('650-700元','675',inplace=True)
df0_1['价格区间'].replace('750-800元','775',inplace=True)
df0_1['价格区间'].replace('600-650元','625',inplace=True)
df0_1['价格区间'].replace('200-250元','225',inplace=True)
df0_1['价格区间'].replace('100元以下','80',inplace=True)
df0_1['价格区间'].replace('700-750元','725',inplace=True)
# print(df0_1)

df0_1.rename(columns={'价格区间':'根据价格区间预估数'},inplace=True)
# print(df0_1)
df0_1[['根据价格区间预估数']]=df0_1[['根据价格区间预估数']].astype(float)
print(df0_1.info())

estimate_Occupy_rate= model.predict(df0_1[['酒店OTA得分']])
print('看看预计的入住率是多少')
print(estimate_Occupy_rate)

df0_1.insert(3,'根据OTA得分预估的入住率',estimate_Occupy_rate)

estimateScore=df0_1['根据价格区间预估数']*df0_1['房间数']*df0_1['根据OTA得分预估的入住率']
print(estimateScore)
df0_1.insert(4,'估计分数=价格估计*房间数*根据OTA得分预估的入住率',estimateScore)
print(df0_1)

print(df0_1['估计分数=价格估计*房间数*根据OTA得分预估的入住率'].describe())

print('答案就是取估计得分的中位数')
print(df0_1['估计分数=价格估计*房间数*根据OTA得分预估的入住率'].median())

df0_1.to_excel('/Users/yangzi/Downloads/近90天内销售发货业务的客户带出OTA房间数房间价格和预估分数.xlsx')


# df0_1.to_excel('/Users/yangzi/Downloads/测试测试.xlsx')

