# f = open("D:\\python_work\\a.txt",'r+') #t表示文本文件方式
# print(f.readline())
# f.write('人工智能')
# f.close()

# f = open("a.txt",'r')
# a = f.read(10)
# print(a)
# f.close()

# f = open("a.txt",'r')
# a = f.readline(9)
# print(a)
# b = f.readline()
# print(b)
# c = f.readline()
# print(c)
# f.close()

# f = open("a.txt",'r')
# a = f.readlines()
# print(a)
# f.seek(0)
# b = f.read()
# print(b)
# f.close()

# f = open("a.txt",'r')
# for line in f:
#    print(line)
# f.close()

# f = open("b.txt",'w')
# f.write('俯首南枝百日枯，半坡古木半坡丛。\n')
# f.write('愿守禅道千年湖，一朝菩提一朝荣。')
# f.close()

# ls = ['俯首南枝百日枯,','半坡古木半坡丛。\n',\
#       '愿守禅道千年湖,','一朝菩提一朝荣。']
# f = open("b.txt",'w')
# f.writelines(ls)
# f.close()


# ls = ['北京', '上海', '天津', '重庆']
# f = open("city.csv", "w")
# # a = ','.join(ls)
# # print(a,type(a))
# f.write(",".join(ls))
# f.close()
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

# f = open("city.csv", "r")
# ls = f.read()
# print(ls)
# ls_new = ls.split(',')
# f.close()
# print(ls_new)

#split() 通过指定分隔符对字符串进行切片,返回列表

ls = [['指标', '2014年', '2015年', '2016年'],
['居民消费价格指数', '102', '101.4', '102'],
['食品', '103.1', '102.3', '104.6'],
['烟酒及用品', '994', '102.1', '101.5'],
['衣着', '102.4', '102.7', '101.4'],
['家庭设备用品', '101.2', '101', '100.5'],
['医疗保健和个人用品', '101.3', '102', '101.1'],
['交通和通信', '99.9', '98.3', '98.7'],
['娱乐教育文化', '101.9', '101.4', '101.6'],
['居住', '102', '100.7', '101.6'],]
# f = open("cpi.csv", "w")
# for row in ls:
#     f.write(",".join(row)+ "\n")
# f.close()



# ls = [['指标', '2014年', '2015年', '2016年'],
# ['居民消费价格指数', '102', '101.4', '102'],
# ['食品', '103.1', '102.3', '104.6'],
# ['烟酒及用品', '994', '102.1', '101.5'],
# ['衣着', '102.4', '102.7', '101.4'],
# ['家庭设备用品', '101.2', '101', '100.5'],
# ['医疗保健和个人用品', '101.3', '102', '101.1'],
# ['交通和通信', '99.9', '98.3', '98.7'],
# ['娱乐教育文化', '101.9', '101.4', '101.6'],
# ['居住', '102', '100.7', '101.6'],]
f = open("cpi.csv", "r")
ls = []
for line in f:
    a= line.strip('\n')
    # print(a)
    b= a.split(',')
    # print(b)
    ls.append(b)
f.close()
print(ls)
