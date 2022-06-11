import requests
r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'
print(r.text)

# f = open('a.txt','r')
# print(f)
# f.read()
# f.write()
# print(r.status_code)

# print(r.encoding)  # HTTP header中猜测的相应内容编码方式
# print(r.apparent_encoding)
# r.encoding = r.apparent_encoding  #当不能使用encoding正确解码时，可以使用apparent_encoding编码方式
# print(r.text)
# print(r.content)
# f1 = open('a.html','w',encoding='utf-8')
# f1.write(r.text)
# f1.close()
# f2 = open('b.html','wb')
# f2.write(r.content)
# f2.close()


'''httpbin返回信息捕获
由客户端向服务端发出，可以分为 4 部分内容：
   请求方法(Request Method) :常见的请求方法有两种 ： GET 和 POST
   请求的网址(Request URL)、 
   请求头(Request Headers) 、用来说明服务器要使用的附加信息
   请求体(Request Body):请求体－般承载的内容是POST请求中的表单数据，而对于GET请求，请求体则为空 
'''
# r = requests.get('http://httpbin.org/get')
# print(r.text)

'''添加额外信息'''
# r = requests.get('http://httpbin.org/get?name=zhangsan&sex=man')
# print(r.text)

'''以字典的形式添加'''
# info ={'name':'zhangsan','sex':'man'}
# r = requests.get('http://httpbin.org/get',params=info)
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))
'''1、运行结果可以判断，请求的链接自动被构造成了：http://httpbin.org/get?name=zhangsan&sex=man
   2、网页的返回类型是str类型,由于httpbin网页返回的格式是Json格式，
      可以直接调用json()方法，得到一个字典格式
      print(type(r.text))
      print(r.json())
      print (type(r.json()))
      注意：需要注意的书，如果返回结果不是JSON格式，便会出现解析错误
'''

'''百度和360搜索如何自动的实现搜索关键词？百度和360搜索为搜索关键词提供了接口'''
'''使用百度关键词爬取'''
# r = requests.get('https://www.baidu.com/s?wd=python')
# r.encoding = r.apparent_encoding
# print(r.text)
# fp = open('d.html','wb')
# fp.write(r.content)
# fp.close()

'''使用360关键词爬取'''
# r = requests.get('https://www.so.com/s?q=java')
# r.encoding = r.apparent_encoding
# print(r.text)
# fp = open('e.html','wb')
# fp.write(r.content)
# fp.close()

'''使用字典的形式爬取'''
# info = {'q':'python'}
# r = requests.get('https://www.so.com/s',params=info)
# r.encoding = r.apparent_encoding
# print(r.text)
# fp = open('c.html','wb')
# fp.write(r.content)
# fp.close()


'''有些网站禁止爬虫爬取内容；例如知乎--发现'''
# head = { "User-Agent": 'Mozilla/5.0'}
# r = requests.get('https://www.zhihu.com/explore',headers = head)
# r.encoding = r.apparent_encoding
# print(r.status_code)
# print(r.text)
# fp = open('e.html','wb')
# fp.write(r.content)
# fp.close()

'''
状态码：https://baike.baidu.com/item/HTTP%E7%8A%B6%E6%80%81%E7%A0%81/5053660?fr=aladdin
'''

'''Post请求：发送数据给服务器'''
'''发送表单数据给httpbin.org/post;注意是post路径
   发送数据给服务器和之前的params参数不同，例如excel里面的表格搜索wangwu
'''

# ls = "python"
# d ={'name':'wangwu','password':'198711'}
# r = requests.post('http://httpbin.org/post', data=d)
# print(r.status_code)
# print(r.text)
#form表单：网页中主要负责数据采集功能

# fp = open('dsdd.txt','w')
''' 发送文件数据给httpbin，可以提交文本、图片、视频、音频等等'''
# fp ={"file":open('bitbug.ico','rb')} #上传图片格式
# r = requests.post('http://httpbin.org/post',files = fp)
# print(r.status_code)
# print(r.text)
# fp = open('e.html','wb')
# fp.write(r.content)
# fp.close()
#数据在files里面




''' 高级用法cookies'''


# head = {
#         'Cookie': '_zap=2583e2f5-a2ef-495e-bf56-204af8baeb28; d_c0="ACBcsl5QxhCPTrXhBNyPCuNjVlqTT0nVM4g=|1580966530"; __guid=74140564.3998529929120890000.1580966531347.7534; z_c0="2|1:0|10:1580979007|4:z_c0|92:Mi4xV203cUVnQUFBQUFBSUZ5eVhsREdFQ1lBQUFCZ0FsVk5QeUVwWHdCNjA2S0hUVzVtWGNhcjZoUFA5ZnRYcUxzY1pR|eb8b5f31b1ea6008e10bb110cbfa47bb5a07cfc36ef18f1cce4ea14e32a271d0"; tst=r; _ga=GA1.2.1474118356.1582863092; _xsrf=gMbQnEVauHdUIF4z9wI73lD8GTCApeQy; _gid=GA1.2.249956259.1583933030; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1583759384,1583933030,1583935494,1583937725; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1583938145; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1583938158|1583935492',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#         }
# r = requests.get('https://www.zhihu.com',headers = head)
# print(r.status_code)
# # print(r.text)
# fp = open('d.html','wb')
# fp.write(r.content)
# fp.close()
# print(r.cookies)
# for key, value in r.cookies.items(): #字典
#     print(key + '=' + value )  #字符串连接


#百度搜索引擎使用
# head ={#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # 'Host': 'www.baidu.com/s',
        # 'Referer': 'http://https://www.baidu.com/',
        # 'Upgrade-Insecure-Requests': '1',
        # 'cookie':'BAIDUID=CDD579B1A91DA27F20A5DB7AE2D9EC70:FG=1; BIDUPSID=CDD579B1A91DA27F20A5DB7AE2D9EC70; PSTM=1580824064; BD_UPN=12314753; BDUSS=FMxSEtNcE4zYkpPTU95ZWJHLWNNSTUxaS11WkV5flVsNkxYeVNmLUwtMXhHWHhlSVFBQUFBJCQAAAAAAAAAAAEAAACNSBoUYW5keWxlbzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHGMVF5xjFRee; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=3; BD_HOME=1; H_PS_PSSID=30963_1464_21091_30842_30794_30823_26350; sugstore=1; BDSVRTM=266',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
       # }
# r = requests.get('http://www.baidu.com/s?w=java',headers = head)
# print(r.status_code)
# fp = open('e.html','wb')
# fp.write(r.content)
# fp.close()

'''美人脸识别程序遭多方起诉 亿万富翁曾用其识别出女儿男朋友身份'''

# import requests
# r = requests.get('http://httpbin.org/cookies/set/number/123456789')
# print(r.text)
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
#
#
# s = requests.session()  #会话维持
# r = s.get('http://httpbin.org/cookies/set/number/123456789')
# print(r.text)
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

'''会话维持-----通常用于模拟登录成功之后再进行下一步的操作'''
# import requests

# class Login(object):
#     '''模拟登录github网页，并爬取登录状态后的settings/profile内容'''
#     def __init__(self):
#         self.headers = {
#             'Referer': 'https://github.com/',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
#             'Host': 'github.com' }
#
#         self.login_url = 'https://github.com/login'
#         self.post_url = 'https://github.com/session'
#         self.logined_url = 'https://github.com/settings/profile'
#         self.session = requests.session()   #会话维持，初始化一个变量session之后都可以使用
#
#     def au_to(self):
#         r = self.session.get(self.login_url, headers=self.headers)
#         print(r.status_code)
#         for line in r.text.split('\n'):
#             if 'authenticity_token' in line:
#
#                 line_new = line.split('value=')[1].split('"')[1]
#         return line_new
#
#     def email_code(self):
#         code = input("请输入邮箱接受到的code:")
#         post_data = {
#             'authenticity_token': self.au_to(),
#             'opt': code }
#         response = self.session.post('https://github.com/sessions/verified-device', data=post_data, headers=self.headers)
#
#     def login(self, login, password):
#         post_data = {
#             'commit': 'Sign in',
#             'authenticity_token': self.au_to(),
#             'ga_id': '2046617795.1581235169',
#             'login': login,
#             'password': password,
#             'webauthn - support': 'supported',
#             'webauthn - iuvpaa - support': 'unsupported',
#             'timestamp': '1584437628798',        #需要修改
#             'timestamp_secret': 'cd72de07996e237def815a29b15a07221d7a5aaefb861dba405c46020679a681'  #需要修改
#         }
#         response = self.session.post(self.post_url, data=post_data, headers=self.headers)
#         print(response.status_code)
#         fp = open('login.html','wb')
#         fp.write(response.content)
#         fp.close()
#         response = self.session.get(self.logined_url, headers=self.headers)
#         print(response.status_code)
#         fp = open('logined.html', 'wb')
#         fp.write(response.content)
#         fp.close()
#
# if __name__ == "__main__":
#     login = Login()
#     login.login(login='andyleo0', password='13365568091zh')



'''
代理服务器
对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，
对于大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，
更甚者可能会直接封禁客户端的IP,导致一定时间段内无法访问 。
'''
import requests
proxie = {'http':'http://115.29.199.16:8118'}

r = requests.get('http://httpbin.org/get',proxies= proxie)
print(r.text)


# r = requests.get('https://www.taobao.com',proxies= proxies)
# print(r.status_code)
# print(r.headers)
# fp = open('proxies.html','wb')
# fp.write(r.content)
# fp.close()

