import random
from _operator import index

num=input("请输入卡片的张数  你要取出的张数 空格隔开")
numres=num.split(" ")
sum=numres[0]
quchusum=int(numres[1])
zimu=input("请输入每张卡片的字母 空格隔开")
zimures=zimu.split(" ")

sum=[]
for i in range(quchusum):
    ran=random.choice(zimures)
    sum+=ran
sum.sort()
# print(sum)
goalsum=0
shang=1
sumnum=[]
for i in sum:
    if i == shang:
        count=sum.count(i)
        # print(count)
        sumnum.append(count)

    else:
        count=1
        # print(count)
        sumnum.append(count)
    shang=i
# print(sumnum)
del sumnum[0]
sumres=0
for i in sumnum:
    sumres+=i*i
print(sumres)
# for i in sum:
#     if i == shang:
#         a = sum.count(i)
#         sumnum.append(a)
#         continue
#     else:
#         a=1
#         sumnum.append(a)
#     shang=i
#
# print(sumnum)
#
# print(goalsum)




print(sum)


