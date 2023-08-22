import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data0=pd.read_excel("/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/取11月有任务的酒店-取门店下有2台以及2台以上机器人的门店房间数分组.xlsx",sheet_name='取11月有任务的酒店-取门店下有2台以及2台以上机器人的门')
print(data0)

print(data0.info())
print(data0.shape)
print(data0)

data0.head(6)

data1=data0[['房间数','日均']]
print(data1)
print('data1的属性是')

print(data1.info())
print(data1.shape)


print('data2的属性是###########################################')
data2=data1.dropna()
print(data2.info())
print(data2.shape)
print(data2)

# data3=data2[:]

plt.figure(num=123)
sns.regplot(data=data2,x="房间数",y="日均")
plt.show()



print("啦啦啦啦啦啦")
