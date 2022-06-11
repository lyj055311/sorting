# 对于字符串，可以逐一遍历字符串的每个字符。
# for c in "Python":
#    print(c)
# print('程序结束')

# 使用range()函数，可以指定语句块的循环次数
# for c in range(1,10,2):  #13579注：切片是[:]
#    print(c)
# print('程序结束')

# break的使用
# for c in "python": # c=t
#    if c == "t":  #True
#        break
#    print(c)
# print('程序结束')

# continue的使用
# for c in "python":  #c =h
#    if c == "t":
#        continue
#    print(c)
# print('程序结束')


# 遍历循环还有一种扩展模式
# for c in "python":  #c =t
#    if c == "t":
#        continue
#    print(c)
# else:
#    print("循环正常结束")
# print('程序结束')


# 嵌套循环
# for i in range(1, 3):  # 1,2 第 2 次循环 i= 2
#     print('外面循环第{}次'.format(i))
#     for j in range(1, 3):  # 1,2第 2次循环 j= 2
#         print('\t内部循环第{}次'.format(j), end='')
#         print('{}*{}={}'.format(i, j, i * j))
# print('程序结束')


#无限循环: while
# n = 0
# while n < 10:  #False
#    print(n)
#    n = n + 3   #n = 12
# print('程序结束')

#无限循环的else扩展模式
# s, num = "py", 0   # s = 'py'  ;num = 0
# while num < len(s):  #len(s) = 2  True
#    print("循环执行中: "+ s[num]) # s[1] = 'y'
#    num += 1    #num = 1
# else:
#    s = "循环正常结束"
# print(s)





#程序的异常处理
# n = eval(input("请输入一个数字: "))
# print(n)


# try:
#    n = eval(input("请输入一个数字: "))
#    print("输入数字的3次方值为: ", n**3)
# except:
#    print("输入错误，请输入一个数字 !")

#通过try 和except实现用户输入数字。
while True:
   try:
       n = eval(input("请输入一个数字: "))
       break
   except:
       print("错误，请输入数字 !")
print("输入数字的为: ", n)
