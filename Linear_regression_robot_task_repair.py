import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df0=pd.read_excel('/Users/yangzi/Downloads/近6个月酒店机器人的任务情况.xlsx')
df0.drop([len(df0)-1],inplace=True)
print(df0.info())
print(df0.tail())
task_daily=df0['任务执行次数']/180
print(task_daily)
df0.insert(3,'日均执行任务次数',task_daily)
print(df0)
print(df0.info())


df1=pd.read_excel('/Users/yangzi/Downloads/近6个月有维修工单的客户 (1).xlsx')
df1.drop([len(df1)-1],inplace=True)
print(df1.info())
print(df1.tail())

df1.rename(columns={'维修工单-终端客户名称':'CRM客户名称'},inplace=True)
print(df1.tail())
print(df1.info())


df0_1=pd.merge(df0,df1,on='CRM客户名称',how='left')
print(df0_1)
print(df0_1.info())

df0_1['维修工单个数'].fillna(value=0,inplace=True)
print('看看合并后的结果是什么')
print(df0_1)
print(df0_1.info())


x = df0_1.loc[:, '日均执行任务次数'].values
y = df0_1.loc[:, '维修工单个数'].values
# 创建模型对象
model = LinearRegression()
# 训练模型
model.fit(x.reshape(-1,1), y)
# fig, ax = plt.subplots()
# plt.figure('看看日均任务和工单数的线性关系图')
fig, ax = plt.subplots()
fig.suptitle('dailytask of robots in hotel and repair times')
ax.scatter(x,y)
ax.text(0.05, 0.95, f"R2: {model.score(x.reshape(-1,1), y)}", ha='left', va='top', transform=ax.transAxes)



# ax.text(0.6, 0.6,str(model.score(x.reshape(-1,1), y)),ha='center', transform=ax.transAxes)
# plt.plot(x,model.predict(x),color='red')
# plt.show()
# # 预测
# new_x =
# y_pred = model.predict([[new_x]])
# print('预测结果：', y_pred)

# 输出斜率、截距和 R2 值
print('斜率：', model.coef_[0])
print('截距：', model.intercept_)
print('R2 值：', model.score(x.reshape(-1,1), y))





plt.figure(num='看看维修工单个数和酒店个数的关系')
ax=sns.countplot(x='维修工单个数',data=df0_1)
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)

# plt.show()

plt.figure(num='看维修工单数为0的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']==0]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1").
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
# plt.show()



plt.figure(num='看维修工单数为1的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']==1]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
# plt.show()



plt.figure(num='看维修工单数为2的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']==2]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
# plt.show()


plt.figure(num='看维修工单数为3的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']==3]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
# plt.show()

plt.figure(num='看维修工单数为4的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']==4]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
# plt.show()


plt.figure(num='看维修工单数为5的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']==5]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
# plt.show()


plt.figure(num='看维修工单数为6和以及以上的酒店,他们的任务分布情况如何')
df0_1_repair0=df0_1[df0_1['维修工单个数']>5]
print(df0_1_repair0)
print(df0_1_repair0.describe())
a=pd.cut(df0_1_repair0['日均执行任务次数'],[1,5,10,20,30,40,50,60,70,80,90,100,1000000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'日均执行任务次数的区间':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.figure(num="日均执行任务次数分布随酒店个数的分布情况")
ax=sns.barplot(x="日均执行任务次数的区间",y="酒店个数",data=e,palette="Set1")
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2, p.get_height() + 0.1, str(p.get_height()), ha='center')
ax.text(0.6, 0.6,str(df0_1_repair0['日均执行任务次数'].describe()),ha='center', transform=ax.transAxes)
plt.show()




#
# df0_1_repair1=df0_1[df0_1['维修工单个数']==1]
# print(df0_1_repair1)
# print(df0_1_repair1.describe())
#
# df0_1_repair2=df0_1[df0_1['维修工单个数']==2]
# print(df0_1_repair2)
# print(df0_1_repair2.describe())
#
# df0_1_repair3=df0_1[df0_1['维修工单个数']==3]
# print(df0_1_repair3)
# print(df0_1_repair3.describe())
#
# df0_1_repair4=df0_1[df0_1['维修工单个数']==4]
# print(df0_1_repair4)
# print(df0_1_repair4.describe())
#
# df0_1_repair5=df0_1[df0_1['维修工单个数']==5]
# print(df0_1_repair5)
# print(df0_1_repair5.describe())
#
# df0_1_repairover5=df0_1[df0_1['维修工单个数']>5]
# print(df0_1_repairover5)
# print(df0_1_repairover5.describe())
#
#






#
#
