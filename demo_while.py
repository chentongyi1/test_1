# num=0
# while num<10:
#     print("hello,world")
#     num+=1

# num=0
# while num<=50:
#     print(num)
#     num+=1
# num=0
# while num<=50:
#     print(num)
#     num+=2
# num=0
# while num<=50:
#     if(num%2==0):
#         print(num)
#     num+=1
# num=50
# #通过start、end、step控制循环语句及循环数据
# while num>=0:
#     print(num)
#     num-=2

# # 循环嵌套
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(i,j," ",sep="",end=" ")
#         j+=1
#     print()
#     i+=1

# # 九九乘法表
# num1=1
# while num1<=9:
#     num2=1
#     while num2<=num1:
#         print("%d*%d=%-2d"%(num2,num1,(num1*num2)),end="  ")
#         num2+=1
#     print(end="\n")
#     num1+=1

# #例子 找出其中的最大数
# list=[2,8,12,43,1,9]
# # #方法一
# # print(max(list))
# # #方法二
# # list.sort()
# # n=len(list)
# # print(list[n-1])
# # #方法三
# # list.sort(reverse=True)
# # print(list[0])
# #方法四 遍历（list里面每个数都判断一下）
# max1=list[0]
# i=0
# while i<len(list):
#     if max1<list[i]:
#         max1=list[i]
#     i+=1
# print(max1)

# # 排序
# list=[2,8,12,43,1,9]
# i=len(list)
# while i>0:
#     j=0
#     while j<i-1:
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
#         j+=1
#     i-=1
# print(list)

# # 倒序排序
# list=[2,8,12,43,1,9]
# i=len(list)
# while i>0:
#     j=0
#     while j<i-1:
#         if list[j+1]>list[j]:
#             list[j],list[j+1]=list[j+1],list[j]
#         j+=1
#     i-=1
# print(list)

# break,continue,else
#
# while True:
#     print("hello,world")
#     break #直接结束循环
# while True:
#     str=input("请输入数字:")
#     if str=="":
#         break
#     else:
#         print(str)

# # continue 结束本次循环，直接开始下次循环
# num1=1
# while num1<=9:
#     if num1==5:
#         num1+=1
#         print("秘密发大财")
#         continue #直接跳过循环后面的语句，不输出5
#     if num1==8:
#         break
#     print(num1)
#     num1+=1
# else: #else受break的影响
#     print("循环结束，以下为无效数字:",num1)

#判断一个数是不是素数----只能被1和自身整除的数 5,11,17(素数或质数)
#方法一
num=2
i=2
while i<num:
    if num%i==0:
        print("%d不是素数"%num)
        break
    i+=1
else:
    print("%d是素数"%num)

#方法二
num2=11
i=2
if num2==1 or num2==2:
    print("%d是素数"%num2)
while i<num2:
    if num2%i==0:
        print("%d不是素数"%num2)
        break
    i+=1
    if i==num2:
        print("%d是素数"%num2)


dict1={"name":"cty","age":16,"score":123}
dict2={"name":"liusi","age":16,"sex":True}
dict3={k:v for k,v in dict1.items() if dict1.get(k)==dict2.get(k)}
print(dict3)