import numpy as np   #

a = np.array([[8,8,8,7,8],
              [9,8,8,8,9],
              [10,9,7,7,8],
              [10,9,8,9,9],
              [10,8,8,8,8]])
# print(a)
# b = [[8,8,8,7,8],
#     [9,8,8,8,9],
#     [10,9,7,7,8],
#     [10,9,8,9,9],
#     [10,8,8,8,8]]
# print(a)
# print(b)
# c = np.random.rand(5,5)
# print(c)
# print(a+c)
# # #
# d = [[8,8,9,7,8],
#     [9,8,8,80,9],
#     [10,9,7,70,8],
#     [10,9,8,9,9],
#     [10,8,8,8,8]]
# print(b+d)
#
# # #numpy更符合数学的运算
# print(a**2)  #  + - * / **
# print(a)
a[0,3] = 11
# print(a)
# print(a[3,3])
print(a.T)
