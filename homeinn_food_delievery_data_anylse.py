import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import time

data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/新建仪表板31 (1).xlsx')
print(data0.head(20))
print(data0.info())

data0.drop_duplicates(subset='创建时间',keep='last',inplace=True)

print(data0.info())

d1=data0['创建时间'].astype('datetime64')
d2=data0['完成时间'].astype('datetime64')
d_d=(d2-d1).dt.seconds
d3=d_d.dropna()
print(d3)
# d4=pd.dataframe(d3)
#
# print(d4.info())
# print(d4.mean)
a=pd.cut(d3,[60,120,180,240,300,360,420,480,540,600,660,720,10000])
b=a.value_counts()
b2=b.sort_index()
print(b2)

c={'时间区间':b2.index,'订单个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.rcParams['font.sans-serif']=['SimHei']
sns.barplot(x="时间区间",y="订单个数",data=e,palette="Set1")
plt.show()



# a=pd.cut(data0_name_room_clear,[0,40,60,80,100,120,150,200,300,500,10000])
# b=a.value_counts()
# b2=b.sort_index()
# print(b2)
# c={'房间数区间分组':b2.index,'酒店个数':b2.values}
# e=pd.DataFrame(c)
# print('e是什么')
# print(e)
#



# print(data0.index)
# print(data0['该订单创建时间'])
# print(data0.info())
#
# data1=data0[['该订单创建时间','后一个订单创建时间']]
# print(data1.head(10))
# print(data1.info())
#
# d1=data1['该订单创建时间'].astype('datetime64')
# d2=data1['后一个订单创建时间'].astype('datetime64')
#
#
