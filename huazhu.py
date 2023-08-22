import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/华住酒店名单和房间组分类-庭锐需求.xlsx')
print(data0.head(20))
data0_clear=data0.dropna()
print(data0_clear)
data0.drop([len(data0)-1],inplace=True)
# data0_name_room=data0[['地点名称','房间数']]
data0_name_room=data0['房间数']
# print(data0_name_room)
data0_name_room_clear=data0_name_room.dropna()
print(data0_name_room_clear)
print(data0_name_room_clear.describe())
data0_name_room_clear.to_excel('/Users/yangzi/Downloads/华住酒店名单和房间组统计-1.xlsx')
a=pd.cut(data0_name_room_clear,[0,40,60,80,100,120,150,200,300,500,10000])
b=a.value_counts()
b2=b.sort_index()
print(b2)
c={'房间数区间分组':b2.index,'酒店个数':b2.values}
e=pd.DataFrame(c)
print('e是什么')
print(e)
# plt.rcParams['font.sans-serif']=['SimHei']
sns.barplot(x="房间数区间分组",y="酒店个数",data=e,palette="Set1")
plt.show()

#################################下面是城市分布的内容

data1_name_cityclass=data0['城市等级']
data1_name_cityclass_clear=data1_name_cityclass.dropna()
print(data1_name_cityclass_clear.head(20))
print(data1_name_cityclass_clear.info())

b1=data1_name_cityclass_clear.value_counts()
print(b1)
plt.rcParams['font.sans-serif']=['SimHei']
sns.barplot(x=b1.index,y=b1.values,data=b1,palette='Set3')
plt.show()
#
# print(b1.info())
# c0=b1.to_frame()
# print(c0)
# c1={'城市等级分组':c0.index,'酒店个数':c0.values}
# print(c1)
# sns.barplot(x="城市等级分组",y="酒店个数",data=c1,palette="Set2")
# plt.show()




















