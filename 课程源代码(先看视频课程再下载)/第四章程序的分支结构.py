# 判断条件及组合
a = 4
# b = 5
# print(a<b,a<=b,a>=b,a>b,a==b,a!=b)
# print('python' > 'pythoN')

# print(not False)
# print((a > 10) or (a > 3 and a < 9))
#        True


# 判断用户输入数字的奇偶性
# s = eval(input("请输出一个整数："))
# if s%2 :    #6%2 =0  = True   False
#     print("这是个奇数")
# print("输入数字是 :", s)
# print('程序结束')


# 判断用户输入数字的特定
# s = eval(input("请输出一个整数："))
# if s % 3 == 0 and s % 5 == 0:  #True
#    print("这个数字既能被3整除，又能被5整除")
# print("输入数字是:", s)



# 判断用户输入数字的某个属性
# s = eval(input("请输出一个整数：")) # s =
# if s % 3 == 0 and s % 5 == 0:      #  s%3 ==0? and s%5 ==0?
#    print("这个数字能够同时被3和5整除")
# else:
#    print("这个数字不能够同时被3和5整除")
# print("输入数字是:", s)



# 判断用户输入数字的某个属性   a = 99 +1
# s = eval(input("请输出一个整数："))
# token = "可以" if s % 3 == 0 and s % 5 == 0 else "不"
# print("这个数字{}能同时被3和5整除 ".format(token))







# 将百分制成绩转换为五分制成绩
score = eval(input("请输出一个百分制成绩："))
if score >= 90.0:
    grade = "A"
elif score >= 80.0:
    grade = "B"
elif score >= 70.0:
    grade = "C"
elif score >= 60.0:
    grade = "D"
else:
    grade = "E"
print("对应的五分制成绩是： {}".format(grade))
