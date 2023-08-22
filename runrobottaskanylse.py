import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from pandas import Series, DataFrame
import time

data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/润在酒店的任务明细2023年2月6日-筛选送物召唤送物美团外卖.xlsx')
# data0.drop([len(data0)-1],inplace=True)
# print(data0.info())
print(data0.head(20))
d1=data0['开始时间'].astype('datetime64')
print('看看d1和data0是什么')
print(d1.info())
print(data0.info())
# data0.astpye(data0['开始时间','结束时间'].astype('datatime64'),inplce=True)

data1=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/2023年2月6日有任务的酒店带出房间数.xlsx')
print(data1.tail(20))
print(data1.describe())
print(data1.info())
data2=data1['房间数'].fillna(127)
print(data2.head(100))
print(data2.describe())

data0_taskid=data0['任务id']
print('机器人任务ID个数')
print(data0_taskid.count())

data0_hotel=data0['云平台名称']
print('酒店的云平台名称')
unique_count_hotel=data0['云平台名称'].nunique()
print(unique_count_hotel)

# import pandas as pd
#
# # Count the unique values in column "col"
# unique_count = df['col'].nunique()
#
# # Print the result
# print("Unique Count:", unique_count)

time_threshold1 = dt.datetime(2023, 2, 6, 14, 0, 0)
time_threshold2 = dt.datetime(2023, 2, 6, 17, 0, 0)
d2=d1[time_threshold1<d1]
print(d2)
d3=d2[d2<time_threshold2]
print(d3)
#
# d4=d3.astype('object')
# d5=d4.pd.Series
#
# print('看看d5是什么')
# print(d5.info())
# print('只取一下开始时间和时长，看看。')
# data0_tran=data0[['任务id','开始时间','时长']]
# print(data0_tran.head(100))
# # data0_tran['开始时间'].astype('datetime64')
# print('看看筛选以后的结果是什么')
#
# d4_merge=pd.merge(left=d4,right=data0_tran,left_on='开始时间',right_on='开始时间')
# print("看看d4 在vlookup以后是什么样子")
# print(d4_merge.head(200))
# data0_tran_d4=data0_tran[data0_tran['开始时间']=d4,:]]
# print(data0_tran_d4.head(100))
# #
# print('只取d3这个时间段的数据，看看是什么样子')
# data0_tran_d3=data0_tran.loc[data0_tran['开始时间']==d4]

# print(data0_tran_d3.head(20))

print("2月6日，放生在14点-17点之间的任务（送物召唤送物外卖多点送物）数为")
print(d3.count())
print('酒店的云平台名称个数，只算有任务的，没任务的不算')
unique_count_hotel=data0['云平台名称'].nunique()
print(unique_count_hotel)
print('这段时间的任务数/酒店个数=店均数量')
averge_task_perhotel=d3.count()/unique_count_hotel
print(averge_task_perhotel)
print('房间数（空值填充为房间数的平均值）的总和是')
print(data2.sum())
print('所以，平均到每间房的房均任务数计算为，房均=任务总数/房间数总和')
averge_task_perroom=d3.count()/data2.sum()
print(averge_task_perroom)



print('以上数据是2月6日周一工作日的数据，如果想看可以操作，我们看看周日weekend的数据是什么样的')

df0=pd.read_excel('/Users/yangzi/Downloads/选取3月5日（周日）的任务情况.xlsx')
df0.drop([len(df0)-1],inplace=True)
print(df0.tail())
print(df0.info())


df1=df0['开始时间'].astype('datetime64')

time_threshold1 = dt.datetime(2023, 3, 5, 14, 0, 0)
time_threshold2 = dt.datetime(2023, 3, 5, 17, 0, 0)

df2=df1[time_threshold1<df1]
# print(d2)
df3=df2[df2<time_threshold2]
print(df3)
print('看看发生在2-5点之间的任务数有多少个吧')
print(df3.count())

print('看看这天有任务的酒店个数有多少个吧')
print(df0['云平台名称'].nunique())

print('看看周日，3月5日，这天，发生在这天2-5点的任务数/酒店个数，是多少。相当于店均多少个送物任务')

print(df3.count()/df0['云平台名称'].nunique())











