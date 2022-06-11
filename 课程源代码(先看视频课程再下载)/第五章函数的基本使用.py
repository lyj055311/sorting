# 例子演示
# for i in range(3):
#     print('人工智能是目前薪资最高的行业！')
#     print('Python 是最接近与人工智能的语言')
#
# for i in range(3):
#     print('人工智能是目前最火热的职业！')
#     print('Python 是最接近与人工智能的语言')
#
# for i in range(3):
#     print('人工智能是目前被关注度最高的行业')
#     print('Python 是最接近与人工智能的语言')
#
# for i in range(3):
#     print('人工智能是未来之光')
#     print('Python 是最接近与人工智能的语言')


# def fact(n):
#     for i in range(3):
#         print(n)
#         print('Python 是最接近与人工智能的语言')
# fact('人工智能是目前薪资最高的行业！')
# fact('人工智能是目前最火热的职业！')
# fact('人工智能是目前被关注度最高的行业')
# fact('人工智能是未来之光')
#
# 简单的函数
# def fact_1():
#     for i in range(4):
#         print('人工智能是目前薪资最高的行业！')
# fact_1()
#
# 定义一个对整数n求阶乘的函数
# def fact_2(n):  # n = 4
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     return s
##
# 调用整数阶乘的函数
#a = fact_2(4)
#print(a)



def peach_heart(a,c,d,e,f,g,b=2):
    print('\n'.join([''.join([(a[(x-y) % len(a)] \
    if ((x*0.04)**2+(y*0.1)**2-1)**3-(x*0.04)**b*(y*0.1)**3\
    <= 0 else ' ') for x in range(-30, 30)]) \
            for y in range(30, -12, -1)]))

peach_heart(a ='angle',c=1,d=2,e=4,5,6,)


# def multiply(x, y = 10):
#     return x*y, x+y
#
# a,b = multiply(99, 2)
# x = 99
# y =2
# a,b = x*y,x+y
# print(a,b)



# 全局变量和局部变量
# def multiply(x, y = 10):
#    z = x*y # z是函数内部的局部变量
#    return z
# s = multiply(99, 2)  #198
# print(s)
# print(z)




# n = 2 #n是全局变量
# def multiply(x, y = 10):
#    global n
#    return x*y*n # 使用全局变量n
# s = multiply(99, 2)
# print(s)



# n = 2  #n是全局变量
# def multiply(x, y = 10):
#     global n
#     n = x*y
#     return n # 此处的n不是全局变量
# s = multiply(99, 2)  #198
# print(s)
# print(n)


import matplotlib.pyplot as plt
plt.figure()
plt.plot([1,2,3,6],[4,5,8,1])
plt.show()
