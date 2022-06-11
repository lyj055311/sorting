d = {'两弹元勋':"邓稼",'青蒿素':"屠呦呦", '水稻之父':"袁隆平"}#陆勇
# print(d,type(d))
# print(d['两弹元勋'])
# d['两弹元勋']= "邓稼先"
# print(d)
# t = {}
# t[201804] = "小新"
# t[201805] = '小强'
# print(t)

d = {"201801":"张三", "201802":"李四", "201803":"王五"}
# a = len(d)
# a = min(d)
# a = max(d)
# a = dict()
# a = d.keys()
# b = list(d.keys())
# a = d.values()
# b = list(d.values())
# a = d.items()
# b = list(d.items())
# a = d.get('201804','没有该元素')
# a = d.pop('201802','没有该元素')
# a = d.popitem()
# print(a)
# d.clear()
# del d["201801"]
# print("201803" in d)
# print(b)
# print(d)
for k in d:  #k ='201802'
    print("字典的键和值分别是：{}和{}".format(k, d.get(k)))