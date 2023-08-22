import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import time

data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/如家1月30日外卖订单时间差超过5分钟明细.xlsx')
print(data0.head(20))

print(data0.index)
print(data0['该订单创建时间'])
print(data0.info())


data1=data0[['该订单创建时间','后一个订单创建时间']]
print(data1.head(10))
print(data1.info())

d1=data1['该订单创建时间'].astype('datetime64')
d2=data1['后一个订单创建时间'].astype('datetime64')
print(d1)
print(d2)

d_d=(d2-d1).dt.seconds
print('我们看看时间差是多少秒啊')
print(d_d)

data1.insert(2,'时间差',d_d)
print(data1)

d_d_5minornot=pd.DataFrame(d_d>300)
print('我们看下大于5分钟的是多少')
print(d_d_5minornot)
print(d_d_5minornot.info())

data1.insert(3,'大于5分钟吗',d_d_5minornot)
print(data1)

data1.to_excel('/Users/yangzi/Downloads/Python输出的结果-如家1月30日外卖订单时间超过5分钟吗.xlsx')





