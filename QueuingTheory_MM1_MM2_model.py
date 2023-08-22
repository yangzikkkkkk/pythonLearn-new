print('参考文献是运筹学中的排队理论，其中MM1模型和MM2模型，我们认为在一个小时内，来到酒店的外卖是随机过程，并且来到酒店的外卖数量满足泊松分布，机器人送外卖送外卖的时间也是彼此间相互独立，如果只有一台机器人，并且是每次只能送一个外卖，则是典型的MM1模型，如果是一次可以送2个外卖，如格格或者UP顶着架子，可以进行为MM2模型')

print('我们来定义一下几个参数')
print('lamada:单位时间内平均到达的外卖数量，平均到达率，时间用分总，所以lamada就是 外卖数每分钟')
print('1/lamada:平均打打间隔时间')
print('miu:单位时间内受到配送的外卖个数，平均服务率，这里是单位实时间由机器人配送的外卖数量，这个是平均服务率')
print('1/miu：平均每个外卖在酒店中的配送时间，这里要注意，算从外卖开始由机器人送，到客人拿，再回来放下架子待命，这段时间的总和')

print('S:服务台个数，在这里，如果酒店只有一个润或者一个UP+单层，此时S=1，这时候就用MM1模型')
print('rou:每个服务台的服务强度，在这里是说每个机器人的服务强度')
print('Pj:在统计平衡的时候，整个系统中有j个外卖的概率')
print('L：队长的期望值，有多少个顾客在系统中，在这里就是有多少个外卖在系统中')
print('Lq：等待队长的期望值，有多少个顾客在排队等待中，在这里就是有多少个外卖在等待被配送')
print('W：逗留时间的期望值，就是一个顾客在系统中从等待到接受服务服务完毕，在系统中逗留的时长的期望值，在这里就是外卖到了酒店送到客户手里到且机器人回来的时间的期望')
print('Wq：等待时间的期望值，就是一个顾客在系统中需要等待接受服务的时间，在这里就是一个外卖送到酒店后等待被配送的时间')

print('ok ,来看看结合具体的事例，以如家万寿路店为例，看看是什么情况')
print('询问了某个酒店(如家万寿路是1小时最多7个，和颐建国门是1小时最多10个)，忙的时候，1个小时，有几个个外卖，来回一趟送物的时长是几分钟，就按照这个思路进行估计')


how_many_food_package_arrive_in_hotel_in_1_hour=8
how_long_would_a_robot_take_the_food_to_customer_and_back_to_station_secends=360


lamada=how_many_food_package_arrive_in_hotel_in_1_hour/60
miufenzhiyi=how_long_would_a_robot_take_the_food_to_customer_and_back_to_station_secends/60
miu=1/miufenzhiyi
rou=lamada/miu
L=rou/(1-rou)
Lq=rou**2/(1-rou)
W=1/(miu-lamada)
Wq=lamada/(miu*(miu-lamada))


print('M/M/1模型计算')
print('那平均送达率，就是每分钟会有多少个外卖')
# print(lamada)
print("{:.2f}".format(lamada))
print('按照1个机器人，送一次外卖需要耗时多少分钟')
# print(miu)
print("{:.2f}".format(miufenzhiyi))
print('平均服务率，就是每分钟系统配送多少个外卖')
# print(miu)
print("{:.2f}".format(miu))
print('系统的服务强度,就是机器人的服务强度')
# print(rou)
print("{:.2f}".format(rou))
print('P0系统稳态的时候没有外卖，所以来了外卖完全不需要等待直接送的概率是')
# print(1-rou)
print("{:.2f}".format(1-rou))
print('稳态的时候L队长的期望值')
# print(L)
print("{:.2f}".format(L))
print('稳态的时候等待队长Lq的期望值')
# print(Lq)
print("{:.2f}".format(Lq))
print('稳态的时候每个外卖在系统中逗留的时间是')
# print(W)
print("{:.2f}".format(W))
print('稳态的时候外卖需要等待的时间是')
# print(Wq)
print("{:.2f}".format(Wq))


print('M/M/2模型计算')
# lamada=7/60
print('每次送2个外卖，近似变成两个柜台，平均每次送物的时间应该是去两个地方后，乘以一个系数1.1')
miufenzhiyi=miufenzhiyi*1.1
miu=1/miufenzhiyi
rou=lamada/(2*miu)
P0=1/(1+2*rou+2*rou**2/(1-rou))
P2=(2*rou)**2/2*P0
L=2*rou+rou*P2/(1-rou)**2
Lq=rou*P2/(1-rou)**2
W=1/miu+rou*P2/(lamada*(1-rou)**2)
Wq=rou*P2/(lamada*(1-rou)**2)


print('那平均送达率，就是每分钟会有多少个外卖')
# print(lamada)
print("{:.2f}".format(lamada))

print('按照2个机器人，送一次外卖需要耗时多少分钟')
# print(miu)
print("{:.2f}".format(miufenzhiyi))
print('平均服务率，就是每分钟系统配送多少个外卖')
# print(miu)
print("{:.2f}".format(miu))
print('系统的服务强度,就是机器人的服务强度')
# print(rou)
print("{:.2f}".format(rou))
print('P0系统稳态的时候没有外卖，所以来了外卖完全不需要等待直接送的概率是')
# print(1-rou)
print("{:.2f}".format(1-rou))
print('稳态的时候L队长的期望值')
# print(L)
print("{:.2f}".format(L))
print('稳态的时候等待队长Lq的期望值')
# print(Lq)
print("{:.2f}".format(Lq))
print('稳态的时候每个外卖在系统中逗留的时间是')
# print(W)
print("{:.2f}".format(W))
print('稳态的时候外卖需要等待的时间是')
# print(Wq)
print("{:.2f}".format(Wq))




print('M/M/3模型计算')
# lamada=7/60
print('用MM3来计算，相当于三台机器人同时工作，同时来配送外卖，用这个效果来评估系统的服务强度等参数，由于三台机器人工作，必然会导致电梯拥堵，所以我们在miufenhziyi这里设大一点，再乘以系数')
miufenzhiyi=miufenzhiyi*1.1
miu=1/miufenzhiyi
rou=lamada/(3*miu)
P0=1/(1+3*rou+(3*rou)**2/2+(3*rou)**3/((3*2)*(1-rou)))
P3=(3*rou)**3/(3*2)*P0
L=3*rou+rou*P3/(1-rou)**2
Lq=rou*P3/(1-rou)**2
W=1/miu+(rou*P3)/(lamada*(1-rou)**2)
Wq=(rou*P3)/(lamada*(1-rou)**2)


print('那平均送达率，就是每分钟会有多少个外卖')
# print(lamada)
print("{:.2f}".format(lamada))
print('按照3个机器人，送一次外卖需要耗时多少分钟')
# print(miu)
print("{:.2f}".format(miufenzhiyi))
print('平均服务率，就是每分钟系统配送多少个外卖')
# print(miu)
print("{:.2f}".format(miu))
print('系统的服务强度,就是机器人的服务强度')
# print(rou)
print("{:.2f}".format(rou))
print('P0系统稳态的时候没有外卖，所以来了外卖完全不需要等待直接送的概率是')
# print(1-rou)
print("{:.2f}".format(1-rou))
print('稳态的时候L队长的期望值')
# print(L)
print("{:.2f}".format(L))
print('稳态的时候等待队长Lq的期望值')
# print(Lq)
print("{:.2f}".format(Lq))
print('稳态的时候每个外卖在系统中逗留的时间是')
# print(W)
print("{:.2f}".format(W))
print('稳态的时候外卖需要等待的时间是')
# print(Wq)
print("{:.2f}".format(Wq))




print('M/M/4模型计算')
# lamada=16/60
print('用MM4来计算，相当于四台机器人同时工作，同时来配送外卖，用这个效果来评估系统的服务强度等参数，由于四台机器人工作，必然会导致电梯拥堵，所以我们在miufenhziyi这里设大一点，乘以系数1.1')
miufenzhiyi=miufenzhiyi*1.1
miu=1/miufenzhiyi
rou=lamada/(4*miu)
P0=1/(1+4*rou+(4*rou)**2/2+(4*rou)**3/(3*2)+(4*rou)**4/((4*3*2)*(1-rou)))
P4=(4*rou)**4/(4*3*2)*P0
L=4*rou+rou*P4/(1-rou)**2
Lq=rou*P4/(1-rou)**2
W=1/miu+(rou*P4)/(lamada*(1-rou)**2)
Wq=(rou*P4)/(lamada*(1-rou)**2)


print('那平均送达率，就是每分钟会有多少个外卖')
# print(lamada)
print("{:.2f}".format(lamada))

print('按照4个机器人，送一次外卖需要耗时多少分钟')
# print(miu)
print("{:.2f}".format(miufenzhiyi))

print('平均服务率，就是每分钟系统配送多少个外卖')
# print(miu)
print("{:.2f}".format(miu))
print('系统的服务强度,就是机器人的服务强度')
# print(rou)
print("{:.2f}".format(rou))
print('P0系统稳态的时候没有外卖，所以来了外卖完全不需要等待直接送的概率是')
# print(1-rou)
print("{:.2f}".format(1-rou))
print('稳态的时候L队长的期望值')
# print(L)
print("{:.2f}".format(L))
print('稳态的时候等待队长Lq的期望值')
# print(Lq)
print("{:.2f}".format(Lq))
print('稳态的时候每个外卖在系统中逗留的时间是')
# print(W)
print("{:.2f}".format(W))
print('稳态的时候外卖需要等待的时间是')
# print(Wq)
print("{:.2f}".format(Wq))




print('M/M/5模型计算')
# lamada=16/60
print('用MM5来计算，相当于5台机器人同时工作，同时来配送外卖，用这个效果来评估系统的服务强度等参数，由于四台机器人工作，必然会导致电梯拥堵，所以我们在miufenhziyi这里设大一点，乘以系数1.1')
miufenzhiyi=miufenzhiyi*1.1
miu=1/miufenzhiyi
rou=lamada/(5*miu)
P0=1/(1+5*rou+(5*rou)**2/2+(5*rou)**3/(3*2)+(5*rou)**4/(4*3*2)+(5*rou)**5/((5*4*3*2)*(1-rou)))
P5=(5*rou)**5/(5*4*3*2)*P0
L=5*rou+rou*P5/(1-rou)**2
Lq=rou*P5/(1-rou)**2
W=1/miu+(rou*P5)/(lamada*(1-rou)**2)
Wq=(rou*P5)/(lamada*(1-rou)**2)

print('那平均送达率，就是每分钟会有多少个外卖')
# print(lamada)
print("{:.2f}".format(lamada))
print('按照5个机器人，送一次外卖需要耗时多少分钟')
# print(miu)
print("{:.2f}".format(miufenzhiyi))

print('平均服务率，就是每分钟系统配送多少个外卖')
# print(miu)
print("{:.2f}".format(miu))
print('系统的服务强度,就是机器人的服务强度')
# print(rou)
print("{:.2f}".format(rou))
print('P0系统稳态的时候没有外卖，所以来了外卖完全不需要等待直接送的概率是')
# print(1-rou)
print("{:.2f}".format(1-rou))
print('稳态的时候L队长的期望值')
# print(L)
print("{:.2f}".format(L))
print('稳态的时候等待队长Lq的期望值')
# print(Lq)
print("{:.2f}".format(Lq))
print('稳态的时候每个外卖在系统中逗留的时间是')
# print(W)
print("{:.2f}".format(W))
print('稳态的时候外卖需要等待的时间是')
# print(Wq)
print("{:.2f}".format(Wq))



