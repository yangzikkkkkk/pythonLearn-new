import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df0=pd.read_excel('/Users/yangzi/Downloads/酒店机器人单次送物任务时长统计.xlsx')
df0.drop([len(df0)-1],inplace=True)
print(df0.head())
print(df0.info())

print(df0['平均送物时长（秒）'].describe())
print(df0['平均送物时长（秒）'].median())

a=pd.cut(df0['平均送物时长（秒）'],[60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960,1020,11131])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'耗时区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
plt.figure(num="送物任务耗时随酒店个数的分布情况")
sns.barplot(x="耗时区间",y="酒店个数",data=e,palette="Set1")

estimate_food_delivery_time=df0['平均送物时长（秒）']*2+11
print(estimate_food_delivery_time)
df0.insert(5,'预估的送外卖时长（送物往返+11秒取）单位秒',estimate_food_delivery_time)
df0.to_excel('/Users/yangzi/Downloads/（估计送一次外卖往返时间）酒店机器人单次送物任务时长统计.xlsx')
plt.show()



