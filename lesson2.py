print("10+20", 10+20)
print("10//20=",10//20)
print("10==20",10==20)
print("10!=20",10!=20)

print("10>20吗？",10>20)

print("-"*100)


print("FOR 循环好用啊")
sum=0
for num in range(1,101):
    sum=sum+num
print("1-100的总和是多少呢，请看",sum)


print("-"*100)

print("while 循环怎么用呢？")
sum=0
num=1
while num<=100:
    sum=sum+num
    num=num+1
print("1-100的总和是，哈哈哈哈",sum)

print("-"*100)





a=45
if a > 50 :
    print("体温已经很高了，一定要注意")
elif a > 40 :
    print("体温还可以，但是也得注意了")
elif a >37 :
    print("你接近了正常了，继续努力下就可以了")
else:
    print("你没啥事，你很正常，别怕了。")

print("%"*100)


def learnpython(loc):
    print("我在{}上学习".format(loc))


learnpython("地铁")
learnpython("树上")
learnpython("图书馆")
