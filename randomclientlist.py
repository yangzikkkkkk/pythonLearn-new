import pandas as pd
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns
import numpy as np


data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/房间数80以上20222023有活动记录.xlsx')
print(data0.head(20))
print(data0.index)
data0.dropna(inplace=True)
print(data0.info())
list=np.random.random_integers(12651,size=1000)
print(list)
data1=data0.iloc[list]
print(data1.head(20))

data_room=data1['房间数']
print(data_room)
cut=pd.cut(data_room,[79,100,120,150,200,250,300,10000])
print(cut)
data1.insert(9,'房间数分组',cut)
print(data1.head(20))
data1.to_excel('/Users/yangzi/Downloads/(随机抽样结果)房间数80以上20222023有活动记录.xlsx')



data2=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/房间数80以上云平台已经成交客户.xlsx')
data2.dropna(inplace=True)
print(data2.head(20))
print(data2.info())

list1=np.random.random_integers(8407,size=1000)
print(list1)

data3=data2.iloc[list1]
print(data3.head(20))

data_room1=data3['房间数']

cut1=pd.cut(data_room1,[79,100,120,150,200,250,300,10000])

data3.insert(8,'房间数分组',cut1)

print(data3.head(20))
print(data3.info())


data3.to_excel('/Users/yangzi/Downloads/(随机抽样结果)房间数80以上云平台已经成交客户.xlsx')
