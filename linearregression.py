import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns
import numpy as np

data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/取11月有任务的酒店-取门店下有2台以及2台以上机器人的门店房间数分组.xlsx')

what_provice_do_you_want='广东省'
# print(data0)
data1=data0[['地点名称','省','市','集团','房间数','日均']]
data1.set_index(['省'],inplace=True)
print('看看data1是什么情况')
# print(data1)
print(data1.index)
print(data1.info())
print(data1.head(10))

data_someprovince=data1[data1.index == what_provice_do_you_want]
print('看看这个省数据吧，没有去掉空置的')
print(data_someprovince)
print(data_someprovince.info())
print(data_someprovince.head(20))
print(data_someprovince.info())

# data_shanghai_clear=data_someprovince.dropna(axis=0,how='any')
# print('datashanghai_clear是什么样呢')
# print(data_shanghai_clear.head(20))


data_someprovince.dropna(axis=0, how='any', inplace=True)
print('这个省的数据去空值以后是什么样呢')
print(data_someprovince.head(20))
print(data_someprovince.info())

# # print(data1)
# # print(data1.info())
# data2=data1.dropna()
# # print(data2)
# print(data2.info())
# print(data2.head(10))
# print(data2.describe())

x=data_someprovince[['房间数']]
y=data_someprovince['日均']

print('x长什么样呢')
print(x)
print(x.info())
print('y长什么样呢')
print(y)
print(y.info())



# data1=data0[['房间数','日均']]
# print(data1)

# data1.head()


# data2=data1.dropna()
# print(data2)
# print(data2.info())
# print(data2.shape)


#
# plt.figure(num=0)
# sns.relplot(data=data2,x='房间数',y='日均')
# plt.show()
#
# print('X和Y 是什么  来出来看看')
# x=data2['房间数']
# y=data2['日均']
#
# x=np.array(x)
# y=np.array(y)
#
# print(x)
# print(y)

# plt.scatter(x,y)
# plt.show()

print('好了，开始建立模型，开始看看')
model=LinearRegression()
model.fit(x,y)

# model.fit(x.reshape(-1,1),y.reshape(-1,1))

y_pred=model.predict(x)
# print(y_pred)
R2=model.score(x,y)
print('R2的值是多少呢，请看')
print(R2)

plt.scatter(x,y)
plt.plot(x,model.predict(x),color='red')
plt.show()

#\
# plt.figure(num=1)
# sns.regplot(data=data2,x='房间数',y='日均')
# plt.show()