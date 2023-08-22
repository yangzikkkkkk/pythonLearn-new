import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/云平台所有门店带房间数2023年2月.xlsx')
data0.drop([len(data0)-1],inplace=True)

# print(data0.head(20))
dataroom=data0[['地点名称','房间数']]
# data0.drop([len(data0)-1],inplace=True)
print(dataroom.tail(20))
dataroom_clear=dataroom.dropna()

# print(dataroom_clear.describe())

# dataroom_clear_room=dataroom_clear['房间数']
dataroom_clear_room=dataroom_clear[dataroom_clear["房间数"]>10]
# dataroom_clear_room=dataroom_clear['房间数']

dataroom_clear_room_onecolum=dataroom_clear_room['房间数']

print(dataroom_clear_room_onecolum.describe())
print('中位数是')
print(dataroom_clear_room_onecolum.median())

#
# import pandas as pd
# df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
# df = df[df.A != 3]




dataroom_clear_room_onecolum.to_excel("/Users/yangzi/Downloads/只有房间数云平台所有门店带房间数2023年2月.xlsx")

# data0_name_room_clear.to_excel('/Users/yangzi/Downloads/华住酒店名单和房间组统计-1.xlsx')
a=pd.cut(dataroom_clear_room_onecolum,[0,40,60,80,100,120,150,200,300,500,10000])
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


#



















