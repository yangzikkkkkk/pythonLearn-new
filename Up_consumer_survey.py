import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df0=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/UP+HDOS清扫和外卖电话调研客户文件-2023年2月初/183UP客户意向调研_.xlsx')

print(df0.head())
print(df0.info())
print(df0['此通电话有效性判断'].describe())
# print(df0['此通电话有效性判断'].isnull)
df0['此通电话有效性判断'].fillna(value='无效沟通',inplace=True)
print(df0['此通电话有效性判断'].tail())

df0_clear=df0[df0['此通电话有效性判断']=='有效沟通']

print(df0_clear.info())
print(df0_clear.head())

df0_clear.fillna(value='Hard to say',inplace=True)
print(df0_clear)
print(df0_clear.columns)


df0_clear_select=df0_clear[['单据编号',  '创建人', '沟通', '创建日期',
       '资料和视频看过后填写，主观感受如何？', '被采访人身份', '是否愿意先付费一个月租金，提前享用',
       '您倾向于买断还是租赁', '您会使用吗',  '对分担酒店工作有帮助吗', '客户名称', '其他信息',
       '倾向于的租赁价格', '倾向于的买断价格', '此通电话有效性判断']]

# df0_clear_select

print(df0_clear_select)

groupnames=[ '创建人', '沟通',
       '资料和视频看过后填写，主观感受如何？', '被采访人身份', '是否愿意先付费一个月租金，提前享用',
       '您倾向于买断还是租赁', '您会使用吗',  '对分担酒店工作有帮助吗',
       '倾向于的租赁价格', '倾向于的买断价格']

for groupname in groupnames:
       grouped = df0_clear_select.groupby(groupname)
       result=grouped['单据编号'].agg(['count',lambda x: x.count()/len(df0_clear_select)])

       # result = grouped.agg({'Quantity': ['count', lambda x: x.count() / len(df)]})

       # result=grouped.count()
       print(groupname)
       print('分类结果')
       result.columns=['Count','Percentage']
       print(result)


df0_clear_select['创建人'].replace('杨子','YZ',inplace=True)
df0_clear_select['创建人'].replace('胡巧玲','QH',inplace=True)

# df0_clear_select['沟通'].replace('不好说','Hard to say',inplace=True)
df0_clear_select['沟通'].replace('可电话直接沟通','Yeah we did have a conversation',inplace=True)
df0_clear_select['沟通'].replace('售后问题','Robots problems',inplace=True)
df0_clear_select['沟通'].replace('售后问题,可电话直接沟通','Robots problems,we did have a conversation ',inplace=True)
df0_clear_select['沟通'].replace('已加微信发资料','Add wechat and sent brief introduction',inplace=True)
df0_clear_select['沟通'].replace('已加微信发资料,售后问题','Robot problem and Add wechat',inplace=True)

df0_clear_select['被采访人身份'].replace('业主','Owner',inplace=True)
df0_clear_select['被采访人身份'].replace('总经理','GM',inplace=True)
df0_clear_select['被采访人身份'].replace('驻店经理','Associate GM',inplace=True)
df0_clear_select['被采访人身份'].replace('其他','Other',inplace=True)
df0_clear_select['被采访人身份'].replace('房务总监','Director of Housekeeping',inplace=True)
df0_clear_select['被采访人身份'].replace('工程总监','Director of EE',inplace=True)


df0_clear_select['是否愿意先付费一个月租金，提前享用'].replace('是','Yes',inplace=True)
df0_clear_select['是否愿意先付费一个月租金，提前享用'].replace('否','No',inplace=True)
# df0_clear_select['是否愿意先付费一个月租金，提前享用'].replace('不好说','Hard to say',inplace=True)

df0_clear_select['您倾向于买断还是租赁'].replace('买断','To buy',inplace=True)
df0_clear_select['您倾向于买断还是租赁'].replace('租赁','To rent',inplace=True)

df0_clear_select['倾向于的租赁价格'].replace('800以内','Less than 800',inplace=True)
df0_clear_select['倾向于的买断价格'].replace('35000以上','Over 35000',inplace=True)



Hotelinfos=pd.read_excel('/Users/yangzi/Library/CloudStorage/Dropbox/云迹科技-Work/18 Temporary&Important/UP+HDOS清扫和外卖电话调研客户文件-2023年2月初/(随机抽样结果)房间数80以上云平台已经成交客户.xlsx')
# print(Hotelinfos.head())
Hotelinfos_rename=Hotelinfos.rename(columns={'CRM客户名称':'客户名称'})
Hotelinfos_rename=Hotelinfos_rename.drop(['Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15'],axis=1)
print(Hotelinfos_rename.head())
print(Hotelinfos_rename.info())
# print(Hotelinfos.columns)
df0_clear_select_Hotelinfos=pd.merge(df0_clear_select,Hotelinfos_rename,on='客户名称',how='left')

print(df0_clear_select_Hotelinfos.info())
print(df0_clear_select_Hotelinfos.head(20))
df0_clear_select_Hotelinfos.dropna(inplace=True)



df0_clear_select_Hotelinfos['城市等级'].replace('一线城市','First class city',inplace=True)
df0_clear_select_Hotelinfos['城市等级'].replace('新一线城市','New First class city',inplace=True)
df0_clear_select_Hotelinfos['城市等级'].replace('二线城市','Second class city',inplace=True)
df0_clear_select_Hotelinfos['城市等级'].replace('三线城市','Third class city',inplace=True)
df0_clear_select_Hotelinfos['城市等级'].replace('四线城市','Fourth class city',inplace=True)
df0_clear_select_Hotelinfos['城市等级'].replace('五线城市','Fifth class city',inplace=True)


df0_clear_select_Hotelinfos['集团分类结果'].replace('三大集团','Big Three',inplace=True)
df0_clear_select_Hotelinfos['集团分类结果'].replace('五大集团','Big Five',inplace=True)
df0_clear_select_Hotelinfos['集团分类结果'].replace('小集团','Small Group',inplace=True)
df0_clear_select_Hotelinfos['集团分类结果'].replace('单体','Single Hotels',inplace=True)



df0_clear_select['您会使用吗'].replace('会','YES',inplace=True)
df0_clear_select['您会使用吗'].replace('不会','NO',inplace=True)
df0_clear_select['您会使用吗'].replace('不好说','Hard to say',inplace=True)



df0_clear_select['对分担酒店工作有帮助吗'].replace('有','YES',inplace=True)
df0_clear_select['对分担酒店工作有帮助吗'].replace('没有','NO',inplace=True)
df0_clear_select['对分担酒店工作有帮助吗'].replace('不好说','Hard to say',inplace=True)




print(df0_clear_select_Hotelinfos[['集团分类结果']].head())
# df0_clear_select_Hotelinfos

df0_clear_select.to_excel('/Users/yangzi/Downloads/UP清洗后的数据.xlsx')
df0_clear_select_Hotelinfos.to_excel('/Users/yangzi/Downloads/UP清洗后的数据-带酒店画像.xlsx')
plt.rcParams.update({'font.size': 8})
# import seaborn as sns
# sns.set(font="Microsoft YaHei")


# plt.rcParams["font.sans-serif"] = ["SimHei"]

print(df0_clear_select)
print(df0_clear_select.columns)

plt.figure(num='总体数据统计')
plt.subplot(3,3,1)
ax=sns.countplot(x='创建人',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['创建人'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('names')
plt.xlabel('Who')
# plt.ylabel('Freq')
# plt.show()

plt.subplot(3,3,2)
ax=sns.countplot(x='沟通',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['沟通'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('communication')
plt.xlabel('different cases')

plt.subplot(3,3,3)
ax=sns.countplot(x='被采访人身份',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['被采访人身份'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('Who are you interviewing')
plt.xlabel('Whom')

plt.subplot(3,3,4)
ax=sns.countplot(x='是否愿意先付费一个月租金，提前享用',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['是否愿意先付费一个月租金，提前享用'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('are you will to pay one month fee to get the robots first')
plt.xlabel('yes or no')

plt.subplot(3,3,5)
ax=sns.countplot(x='您倾向于买断还是租赁',data=df0_clear_select)
total_count=len(df0_clear_select['您倾向于买断还是租赁'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('To buy or to rent')

plt.subplot(3,3,6)
ax=sns.countplot(x='倾向于的租赁价格',data=df0_clear_select)
total_count=len(df0_clear_select['倾向于的租赁价格'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('prices to rent')

plt.subplot(3,3,7)
ax=sns.countplot(x='倾向于的买断价格',data=df0_clear_select)
total_count=len(df0_clear_select['倾向于的买断价格'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('prices to buy')

plt.tight_layout()
# plt.show()



plt.figure(num='客户的初步意愿统计')
plt.subplot(2,2,1)
ax=sns.countplot(x='对分担酒店工作有帮助吗',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['对分担酒店工作有帮助吗'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('Will the robot help?')
# plt.xlabel('Who')


plt.subplot(2,2,2)
ax=sns.countplot(x='您会使用吗',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['您会使用吗'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('Will Your Hotel use this robot?')



plt.subplot(2,2,3)
ax=sns.countplot(x='是否愿意先付费一个月租金，提前享用',data=df0_clear_select)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
total_count=len(df0_clear_select['是否愿意先付费一个月租金，提前享用'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
plt.title('Will you pay one month fee to install the robot first?')






plt.figure(num="客户画像分析-倾向购买")
plt.subplot(2,2,1)
ax=sns.countplot(x='城市等级',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['您倾向于买断还是租赁']=='To buy'])
total_count=len(df0_clear_select_Hotelinfos['城市等级'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('in What citeis the hotel prefer "To buy" ')


plt.subplot(2,2,2)
ax=sns.countplot(x='集团分类结果',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['您倾向于买断还是租赁']=='To buy'])
total_count=len(df0_clear_select_Hotelinfos['集团分类结果'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What kind group of hotel prefer "To buy" ')


plt.subplot(2,2,3)
ax=sns.countplot(x='房间数分组',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['您倾向于买断还是租赁']=='To buy'])
total_count=len(df0_clear_select_Hotelinfos['房间数分组'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What kind Rooms level of hotel prefer "To buy" ')


plt.figure(num="客户画像分析-倾向租赁")

plt.subplot(2,2,1)
ax=sns.countplot(x='城市等级',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['您倾向于买断还是租赁']=='To rent'])
total_count=len(df0_clear_select_Hotelinfos['城市等级'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('in What citeis the hotel prefer "To Rent" ')


plt.subplot(2,2,2)
ax=sns.countplot(x='集团分类结果',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['您倾向于买断还是租赁']=='To rent'])
total_count=len(df0_clear_select_Hotelinfos['集团分类结果'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What kind group of hotel prefer "To rent" ')


plt.subplot(2,2,3)
ax=sns.countplot(x='房间数分组',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['您倾向于买断还是租赁']=='To rent'])
total_count=len(df0_clear_select_Hotelinfos['房间数分组'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What kind Rooms level of hotel prefer "To buy" ')


plt.figure(num="客户画像分析购买价格倾向高于2.5万")

To_buy_price_accepted=['25000-30000','30000-35000','Over 35000']

plt.subplot(2,2,1)
ax=sns.countplot(x='城市等级',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['倾向于的买断价格'].isin(To_buy_price_accepted) ])
total_count=len(df0_clear_select_Hotelinfos['城市等级'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('in What citeis the hotel prefer "To buy over 25000 Yuan" ')


plt.subplot(2,2,2)
ax=sns.countplot(x='集团分类结果',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['倾向于的买断价格'].isin(To_buy_price_accepted) ])
total_count=len(df0_clear_select_Hotelinfos['集团分类结果'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What kind group of hotel prefer "To buy over 25000 Yuan" ')



plt.subplot(2,2,3)
ax=sns.countplot(x='房间数分组',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['倾向于的买断价格'].isin(To_buy_price_accepted) ])
total_count=len(df0_clear_select_Hotelinfos['房间数分组'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What Rooms level of hotel prefer "To buy over 25000 Yuan" ')



plt.figure(num="客户画像分析租赁价格高于1500元/月")
To_rent_price_accepted=['1500-1800','1800-2000','2500-3000','3000-4000']

plt.subplot(2,2,1)
ax=sns.countplot(x='城市等级',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['倾向于的租赁价格'].isin(To_rent_price_accepted) ])
total_count=len(df0_clear_select_Hotelinfos['城市等级'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('in What citeis the hotel prefer "To rent over 1500YUAN/Month" ')


plt.subplot(2,2,2)
ax=sns.countplot(x='集团分类结果',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['倾向于的租赁价格'].isin(To_rent_price_accepted) ])
total_count=len(df0_clear_select_Hotelinfos['集团分类结果'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What kind group of hotel prefer "To rent over 1500YUAN/Month" ')


plt.subplot(2,2,3)
ax=sns.countplot(x='房间数分组',data=df0_clear_select_Hotelinfos[df0_clear_select_Hotelinfos['倾向于的租赁价格'].isin(To_rent_price_accepted) ])
total_count=len(df0_clear_select_Hotelinfos['房间数分组'])
for p in ax.patches:
       proportion = p.get_height()/total_count
       # ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.9, p.get_height(), ha='center'           )
       ax.text(p.get_x()+p.get_width()/2, p.get_height() +0.1,f"{p.get_height()}({proportion:.2%})", ha="center")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.title('What Rooms level of hotel prefer "To rent over 1500YUAN/Month" ')

plt.tight_layout()
plt.show()


