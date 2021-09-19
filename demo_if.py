#控制语句 -- 条件、循环
#if
# score=float(input("请输入成绩:")) #input输入的是字符串
# if score>=60:
#     print("及格")
# else:
#     print("不及格")
# if score>=60:
#     print("恭喜通过")
# else:
#     pass
# if score<60:
#     print("不及格")
# if score>=60 and score<90:
#     print("良好")
# if score>=90:
#     print("优秀")

# if score<60:
#     print("不及格")
# elif score<90:
#     print("良好")
# else:
#     print("优秀")

# if score>=60:
#     if score<90:
#         print("良好")
#     else:
#         print("优秀")
# else:
#     print("不及格")

#多分支条件优化，删掉隐含条件
# if score<0 or score>100:
#     print("非法")
# elif score<60:
#      print("不及格")
# elif score<90: #隐含条件,这里等价于if score>=60 and score<90
#     print("良好")
# else:
#     print("优秀")

#嵌套
#登录是否成功 account:admin, password:123456
# account=input("请输入帐号:")
# password=input("请输入密码:")
# if account=="admin":
#     if password=='123456':
#         print("登录成功")
#         pass
#     else:
#         print("密码错误")
#         pass
# else:
#     print("帐号不存在")
#     pass
