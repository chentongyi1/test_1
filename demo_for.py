#coding:utf8
#for循环遍历
import random

list1=[2,8,12,43,1,9]
name="Python Tes"
tuple1=("zhangsan","lisi","wangwu",2,3,4,True)
set1={"zhangsan","lisi","wangwu","zhangsssss","lisi"}
dict1={"name":"zhangsan","age":33,"sex":True,"depart":"技术部"}
# for ele in dict1: #遍历dict的key
#     print(ele)
# for ele in dict1.keys():
#     print(ele)
# for ele in dict1.values():
#     print(ele)
# for ele in dict1.items():
#     print(ele)#得到的元素是一个tuple
#     print(ele[0])
# for key,value in dict1.items():
#     print(key,":",value)
# for ele in dict1.items():
#     print(ele[0],":",ele[1])
# max=0
# for l in list1:
#     if max<l:
#         max=l
# print(max)
#
# list1=[1,2,3,4,5,6,7,8,9]
# list2=[1,2,3,4,5,6,7,8,9]
# for i in list1:
#     for j in list2:
#         if j>i:
#             break
#         else:
#             print(i,j,sep="",end=" ")
#     print()


# #range函数---range---序列对象(多个数据，整数 数值)  rang(n) 0到n的整数，不包含n，获取[start,end)的整数
# #不要把list等关键字定义为变量!!!
# list1=list(range(5))
# print(list1)
#
# print(range(-10,10))
# print(list(range(-10,10)))
#
# #start,end,step --
# print(list(range(-10,10,2)))

#打印10次"hello,world"
# for l in range(0,10,2):
#     print(l)
#     print("hello,world")
# print(random.random())#random()函数，随机生成一个实数，范围[0,1)
# #range(n),[0,n)的整数

# num=int(random.random()*100)
# print(num)



#打印圣诞树,第6层，最后一层有10个
'''
  *   *号个数等于行数，*号前空格数等于行数-该行星号个数  3-1
 * *
* * *  
'''
#方法一
print("打印圣诞树第一种方法:")
lines=4
for num in range(1,lines+1):
    print(" "*(lines-num),"* "*(num),sep="")
#方法二
print("打印圣诞树第二种方法:")
lines=3
line=1
while line<=lines:
    print(" "*(lines-line),"* "*(line),sep="")
    line+=1
#方法三
print("打印圣诞树第三种方法:")
lines=6
for line in range(1,lines+1):
    list1=[]
    list1.append(" "*(lines-line))
    list1.append("* "*line)
    for str1 in list1:
        print(str1,end="")
    print()


# list1=[]
# list1.append("* "*3)
# print(list1)

# list1=[]
# list1.append(" "*3)
# print(list1)
# for str2 in list1:
#     print(str2,"a")
#其他使用

#九九乘法表,记住，不要搞出重复的!!!没有81个算式!!!
#方法一
for m in range(1,10):
    for n in range(1,m+1):
        print("%d*%d=%-2d"%(n,m,(n*m)),end=" ")
    print()
else:
    print("以上为完整的九九乘法表")
# #方法二
# line=1
# while line<=9:
#     for num in range(1,line+1):
#         print("%d*%d=%-3d"%(num,line,num*line),end=" ")
#     print()
#     line+=1

#推导，python特色
list1=[1,4,6,9,23,10]
list2=[ele**2 for ele in list1]
print(list2)

list3=[ele*ele for ele in list1 if ele%2==0]
print(list3)

list4=[ele**2 for ele in list1 if ele==1 or ele==9]
print(list4)

list5=[ele**2 for ele in list1 if ele in range(10)]
print(list5)


set1={1334,4,6,7,7,8,2,3}
set2={s for s in set1}
print(set2)

dict1={"name":"zhangsang","age":13,"sex":True}
dict2={k:v for k,v in dict1.items()} #字典dict推导式
print(dict2)