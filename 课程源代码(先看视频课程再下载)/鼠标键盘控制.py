'''18.1'''

# import pyautogui
# 获取当前屏幕分辨率
# print(pyautogui.size())
# x,y = pyautogui.size()
# print(x,y)

'''18.2.2获取当前鼠标位置'''
# import pyautogui
# import time
# time.sleep(2)
# print(pyautogui.position())
# x,y = pyautogui.position()
# print(x,y)

'''18.2.3获取当前鼠标位置'''
# 2秒钟鼠标移动坐标为100,500位置  绝对移动
# import pyautogui
# pyautogui.moveTo(100,500,2,logScreenshot= True)



# import pyautogui
# pyautogui.move(100,500,2,logScreenshot= True)




# import pyautogui
# print(pyautogui.onScreen(1900,1000))








'''18.2.4鼠标左击一次'''

# import pyautogui
# pyautogui.click(500, 200,duration=3)
# pyautogui.click(button='left', clicks=3, interval=0.2)
# pyautogui.click(button='right')

#借助画图工具
# import pyautogui
# import time
# time.sleep(3)
# pyautogui.click(150,450,clicks = 2)

# import time
# import pyautogui
# time.sleep(4)
# pyautogui.click(x=433, y=213,clicks=2)




# import pyautogui
# import time
# time.sleep(3)
# pyautogui.doubleClick(150,450)




# import pyautogui
# pyautogui.mouseDown()
# pyautogui.mouseUp()




''''绘制五角星'''
# import time
# import pyautogui
# time.sleep(5)
# location = [(555,380),(844,380),(610,547),(700,272),(790,546),(555,380)]
# for i in range(len(location)-1):
#     pyautogui.mouseDown(location[i])
#     pyautogui.mouseUp(location[i+1])





'''18.2.5 拖拽鼠标'''
# import pyautogui
# import time
# time.sleep(3)
# pyautogui.dragTo(400, 200,duration=1.0, button="left" )





'''18.2.6'''
import time
import pyautogui
import pytweening
time.sleep(3)
pyautogui.dragTo(300,200,duration=3,tween =pytweening.easeInElastic )
#easeInQuad：表示鼠标移动开始缓慢，之后逐渐加速。
# easeOutQuad：表示鼠标移动开始快速，之后逐渐减速。
# easeInElastic：表示开始时抖动移动，然后突然直线进入目的地



'''18.2.7'''
# import pyautogui
# import time
# time.sleep(2)
# pyautogui.scroll(-1080)



'''18.3.1'''
# import pyautogui
# pyautogui.write('Hello world')


'''18.3.2'''
# import pyautogui
# pyautogui.press('down',presses=3)     #KEYBOARD_KEYS
# pyautogui.keyDown('ctrl')
# pyautogui.press('c')        #复制
# pyautogui.keyUp('ctrl')



'''18.3.3 组合快捷键'''
# import pyautogui
# pyautogui.hotkey('ctrl', 'c',interval=1)



'''18.3.4'''
# import pyautogui
# print(pyautogui.isValidKey('f1'))

# import pyautogui
# pyautogui.screenshot('hello.png')




# import pyautogui
# pyautogui.alert('报错:您输入的键不正确')


# import pyautogui
# pyautogui.run('g300,670ll')#鼠标移动到300，670的位置，并左击鼠标2次



'''18.4'''
import pyperclip
import pyautogui
pyperclip.copy('实现中文写入到剪贴板中')
# pyautogui.hotkey('ctrl', 'v',interval=1)
print(pyperclip.paste())




# import pyperclip
# import pyautogui
# import time
# time.sleep(3)
# pyperclip.copy('更改鼠标设置')
# pyautogui.click(720,200)
# pyautogui.hotkey('ctrl', 'v',interval=1)
# pyautogui.click(720,250)


'''批量打印文档'''
# import pyperclip
# import openpyxl
# import pyautogui
# import time
# wb = openpyxl.load_workbook('2021级计算机学院成绩统计.xlsx')
# wb_sheet = wb['成绩']
# for student in wb_sheet['A2':'D50']:
#     i =0
#     y_addr = 400
#     for one_cell in student:
#         y_addr +=  i*50
#         pyautogui.click(950, y_addr)
#         pyperclip.copy(one_cell)
#         pyautogui.hotkey('ctrl', 'v',interval=0.5)
#         i += 1
#     pyautogui.click(950, 680)
#     time.sleep(5)




#实现有道词典中的翻译项目
# import pyautogui
# import pyperclip
# import time
# time.sleep(3)
# pyautogui.doubleClick(150,450)  #打开有道词典
# f_1 = open(r'C:\Users\Administrator\Desktop\中文翻译.txt','r',encoding='utf-8')#打开待翻译的文件
# f_2 = open(r'C:\Users\Administrator\Desktop\中文翻译后.txt','w',encoding='utf-8')#打开待翻译的文件
#
# for line in f_1:
#     f_2.write(line)
#     if line !='\n':     #获取到非空白行的内容
#         pyperclip.copy(line)    #将一行内容写入到内存中
#         pyautogui.click(800, 300,clicks = 3,interval=0.2)   #全选中框内中文，为下一次粘贴做准备
#         pyautogui.hotkey('ctrl', 'v',interval=0.2)    #将中文粘贴到框内
#         time.sleep(1) #等待翻译时间
#         pyautogui.click(800, 880)   #复制翻译后的内容
#         f_2.write(pyperclip.paste()+'\n')
# f_1.close()
# f_2.close()

