# s = {1010, 'def', 78.9,'76.8',78.9}
# print(s)
# print(type(s))




##集合类型有4个操作符
# s = {1010, "python", 78.9}
# t = {1010, "set", 12.3, 1010, 1010}
# print(s - t)
# print(s & t)
# print(s ^ t)
# print(s | t)



#集合类型有一些常用的操作函数或方法
# s = {1010, "python", 78.9}
# s.add('人工智能')
# s.remove(1010)
# s.clear()
# print(len(s))
# print(1010 in s)
# print(1010 not in s)
# print(s)


#set()函数
# a = set()
# print(a)
# s = set('知之为知之不知为不知')
# print(s)



# ls = ['甜甜圈','珍珠奶茶','方便面', "卡路里", 101]
# print(ls,type(ls)) int float str()  set()
# print(list('列表可以由字符串生成'))
# ls = [1010, "1010", [1010, "1010"], 1010]
# print(ls[3])
# print(ls[-2])
# print(ls[5])
# for i in ls:  #i  = 1010
#    print(i*2)
# ls = [1010, "1010", [1010, "1010"], 1010]
# print(ls[1:4])
# print(ls[-3:-1])
# print(ls[0:4:2])


ls = ['风清扬','令狐冲','东方不败','杨过','东方不败'] #5643
# ls.append('欧阳锋')
# lt = ['萧峰','独孤求败']
# ls += lt  # ls = ls +lt
# ls.insert(1,'郭靖')
# ls.clear()
# print(ls.pop(1))
# ls.remove("东方不败")
# del ls[1:3]
# del ls[1:]
# print(ls.reverse())
# lt = ls.copy()   #lt = 5644  =>['风清扬','令狐冲','东方不败','杨过']/
# ls.clear() # 清空ls
# print(lt)
# ls[1] = '独孤求败'
# print(ls)


#元组
ls = ('风清扬','令狐冲','东方不败','杨过','东方不败')
# print(ls,type(ls))
# print(ls.count('东方不败'))
# print(ls.index('东方不败'))
# print(ls[1])
# lt = ['风清扬','令狐冲','东方不败']
lp = '十大武林高手'
# print(tuple(lt))
print(tuple(lp))