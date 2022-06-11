

'''16.2.1'''
import poplib
mailpop = poplib.POP3_SSL('pop.sina.com')   #POP3服务器地址
a = mailpop.user('chaoxiangedu@sina.com')   #账户名
b = mailpop.pass_('1bc9624d4ec512a9')       #授权码
print(a,'\n',b,'\n',mailpop)




'''16.2.2 获取邮箱中的邮件'''
# import poplib
# mailpop = poplib.POP3_SSL('pop.sina.com')
# mailpop.user('chaoxiangedu@sina.com')
# mailpop.pass_('1bc9624d4ec512a9')
# a = mailpop.list(2)      #返回邮件对象  open  文件
# print(a)


'''获取邮件内容'''
# import poplib
# mailpop = poplib.POP3_SSL('pop.sina.com')
# mailpop.user('chaoxiangedu@sina.com')
# mailpop.pass_('1bc9624d4ec512a9')
# mail = mailpop.retr(3)
# print(mail)
#包含3部分的数据内容。
# 第1部分表示邮件对象获取成功，且文件内容为2635字节大小，即图中b'+OK 2635 octets'。
# 第2部分为邮件的信息，邮件信息为一个列表类型（其中又包含了2部分，第1部分为邮件接收信息，邮箱服务器的MID、邮件类型、内容类型、邮件摘要、邮件接收人和邮件发送人信息等。第2部分为邮件主体部分）。
# 第3部分为邮件内容的字节总数。


'''16.2.3下载邮件内容'''
# import poplib
# mailpop = poplib.POP3_SSL('pop.sina.com')
# mailpop.user('chaoxiangedu@sina.com')
# mailpop.pass_('1bc9624d4ec512a9')
# mail = mailpop.retr(1)[1]
# f= open('邮件.html','wb')
# for line in mail:
#     f.write(line)
# f.close()




'''16.2.4'''
# import poplib
# import re
# mailpop = poplib.POP3_SSL(host='pop.sina.com')
# mailpop.user(user='chaoxiangedu@sina.com')
# mailpop.pass_( pswd='89a4becf383cfd42')
# a = mailpop.list()
# for i in range(1,len(a[1])+1):
#     mail = mailpop.retr(which=str(i))[1]
#     for line in mail:
#         if 'X-Sender:' in str(line):
#             print(re.findall('X-Sender: (.+)\'', str(line)))
#             break
#         if 'From:' in str(line):
#             print(re.findall('From: .+<(.+)>', str(line)))
#             break









'''16.3.1'''
# import smtplib
# mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
# mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
# print(mailsmtp)


'''16.3.3'''
# import smtplib
# from email.mime.text import MIMEText
# mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
# mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
# msg = MIMEText('学习邮件发送', 'plain', 'utf-8')
# msg['Subject'] = 'Python办公自动化'          #添加邮件主题
# msg['from'] = 'chaoxiangedu@sina.com'      #添加邮件发送人
# mailsmtp.sendmail('chaoxiangedu@sina.com', '13672090629@sina.cn', msg.as_string())
# 参数msg.as_string()表示以字符串形式返回整个格式化消息



'''16.3.4'''
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
# mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
# meg = MIMEMultipart()    #构建一个多模块邮件对象
# meg.attach(MIMEText('正在学习邮件收发', 'plain', 'utf-8'))
# meg['From'] = 'chaoxiangedu@sina.com'
# meg['Subject'] = 'Python办公自动化'
# att1 = MIMEText(open('a.txt', 'rb').read(), 'plain', 'utf-8')
# att1["Content-Disposition"] = 'attachment; filename="a.txt"'#attachment表示以附件的形式
# meg.attach(att1)
# mailsmtp.sendmail('chaoxiangedu@sina.com', '13672090629@sina.cn', meg.as_string())


'''实验'''
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
#
# mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
# mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
# meg = MIMEMultipart()    #构建一个多模块邮件对象
# meg['From'] = 'chaoxiangedu@sina.com'
# meg['Subject'] = 'Python办公自动化'
# meg.attach(MIMEText('正在学习邮件收发', 'plain', 'utf-8'))
# att1 = MIMEApplication(open('实验3.docx', 'rb').read())
# att1["Content-Disposition"] = 'attachment; filename="shiyan3.docx"'  #不支持中文显示
# meg.attach(att1)
# mailsmtp.sendmail('chaoxiangedu@sina.com', '13672090629@sina.cn', meg.as_string())




'''16.3.5'''
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
# mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
# meg = MIMEMultipart()
# meg['From'] = 'chaoxiangedu@sina.com'
# meg['Subject'] = 'Python办公自动化'
# meg.attach(MIMEText('正在学习邮件收发', 'plain', 'utf-8'))
# att1 = MIMEImage(_imagedata = open('识图.jpg','rb').read())
# att1["Content-Disposition"] = 'attachment; filename="shitu.jpg"'
# meg.attach(att1)
# mailsmtp.sendmail('chaoxiangedu@sina.com', '13672090629@sina.cn', meg.as_string())



'''16.6'''
#项目1
# import os
# import docx
# import re
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
# mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
# meg = MIMEMultipart()
# meg['From'] = 'chaoxiangedu@sina.com'
# meg['Subject'] = 'Python办公自动化'
# for file_name in os.listdir('./数据3'):
#     file_adr = './数据3/'+ file_name
#     docD = docx.Document(file_adr)
#     result = re.findall('地址：(.+)',docD.paragraphs[0].text)
#     meg.attach(MIMEText('请您查收汽车文档说明书', 'plain', 'utf-8'))
#     att = MIMEText(open(file_adr, 'rb').read(), 'base64', 'utf-8')
#     meg.attach(att)
#     mailsmtp.sendmail('chaoxiangedu@sina.com', result[0], meg.as_string())
#     meg._payload.clear()



#项目2
# import os
# import openpyxl
# import smtplib
# import time
# from email.mime.text import MIMEText
# for file_name in os.listdir('./数据3/工资'): #遍历文件夹中的所有文件
#     file_adr = './数据3/工资/'+ file_name   #获取每个文件的地址
#     wb = openpyxl.load_workbook(file_adr)   #读取每个excel文件
#     wb_sheet = wb.active        #获取工作表
#     for i in range(wb_sheet.min_row+1,wb_sheet.max_row+1):#遍历工作表中存在数据的每一行
#         sub = '{}本月的工资单'.format(wb_sheet['A'+str(i)].value)#员工姓名
#         info = '{}您好：\n这是本月的工资单明细：'.format(wb_sheet['A'+str(i)].value)
#         for j in range(wb_sheet.min_column,wb_sheet.max_column):#遍历工作表中存在数据的每一列
#             j = openpyxl.utils.get_column_letter(j) #获取列号
#             # print(wb_sheet[j+str(i)].value)
#             if wb_sheet[j+'1'].value == '邮箱地址':  #找到邮箱地址单元格
#                 addr = wb_sheet[j+str(i)].value   #获取单元格为ij的内容
#                 continue
#             info += '{}:{}\t'.format(wb_sheet[j+'1'].value,wb_sheet[j+str(i)].value)    #其它信息
#         print(sub)
#         print(info)
#         print(addr)
#         mailsmtp = smtplib.SMTP_SSL('smtp.sina.com')
#         mailsmtp.login('chaoxiangedu@sina.com', '1bc9624d4ec512a9')
#         msg = MIMEText(info, 'plain', 'utf-8')
#         msg['Subject'] = sub
#         msg['from'] = 'chaoxiangedu@sina.com'
#         mailsmtp.sendmail('chaoxiangedu@sina.com', addr, msg.as_string())
#         mailsmtp.close()
#         time.sleep(3)
#     wb.close()