import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/取11月有任务的酒店-取门店（测试导出-1.xlsx')
print(df.head(20))
print(df.info())

df_clear=df.dropna()
print(df_clear.info())
print(df_clear.tail(20))

print(df_clear['酒店星级1'])

df_clear['酒店星级1'].replace('三星',3,inplace=True)
df_clear['酒店星级1'].replace('四星',4,inplace=True)
df_clear['酒店星级1'].replace('五星',5,inplace=True)
df_clear['酒店星级1'].replace('经济型',2,inplace=True)
# print(df_clear['酒店星级1'])
df_clear['城市等级'].replace('一线城市',10,inplace=True)
df_clear['城市等级'].replace('新一线城市',8,inplace=True)
df_clear['城市等级'].replace('二线城市',6,inplace=True)
df_clear['城市等级'].replace('三线城市',4,inplace=True)
df_clear['城市等级'].replace('四线城市',2,inplace=True)
df_clear['城市等级'].replace('五线城市',1,inplace=True)
# print(df_clear['城市等级'])
# print(df_clear[['酒店星级1','城市等级']].head(200))
df_clear.to_excel('/Users/yangzi/Downloads/(转化后的结果)取11月有任务的酒店-取门店（测试导出）.xlsx')

reg=linear_model.LinearRegression()
reg.fit(df_clear[['酒店星级1','城市等级','酒店OTA得分','该门店多少台机器人','房间数']],df_clear['日均'])

print(reg.coef_)
print(reg.intercept_)

R2=reg.score(df_clear[['酒店星级1','城市等级','酒店OTA得分','该门店多少台机器人','房间数']],df_clear['日均'])
print('R2的值是多少呢，请看')
print(R2)

plt.figure(num='城市等级，酒店星级，OTA得分，门店机器人数量对机器人日均任务的影响')
plt.subplot(3,2,1)
plt.scatter(df_clear['城市等级'],df_clear['日均'])
plt.title("city class (city score)-dailytask")
# plt.show()

plt.subplot(3,2,2)
plt.scatter(df_clear['酒店星级1'],df_clear['日均'])
plt.title("stars of hotel-dailytask")


plt.subplot(3,2,3)
plt.scatter(df_clear['酒店OTA得分'],df_clear['日均'])
plt.title("OTA score (from ctrip)-dailytask")

plt.subplot(3,2,4)
plt.scatter(df_clear['该门店多少台机器人'],df_clear['日均'])
plt.title('num of robots-dailytask')


plt.subplot(3,2,5)
plt.scatter(df_clear['房间数'],df_clear['日均'])
plt.title('rooms of hotel-dailytask')

plt.subplot(3,2,6)
sns.regplot(df_clear,x=df_clear['房间数'],y=df_clear['日均'])
plt.title('with linear regression, also rooms of hotel-dailytask')

# plt.tight_layout()
plt.show()


# sns.regplot(df_clear,x=df_clear['该门店多少台机器人'],y=df_clear['日均'])
# plt.show()