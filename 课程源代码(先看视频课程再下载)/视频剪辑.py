'''19.2.1'''
# from moviepy.editor import VideoFileClip
# clip = VideoFileClip("Python表达式.mp4",)
# print(clip)
# print(clip.duration,clip.end,clip.fps,clip.size,clip.rotation,clip.filename)
# （1）duration：视频的时间长度，单位为秒。
# （2）end：视频结束时间，单位为秒。
# （3）fps：视频的帧速率。
# （4）size：视频尺寸大小。
# （5）rotation：视频旋转角度。
# （6）filename：视频文件名称。




'''19.2.2'''
# from moviepy.editor import VideoFileClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip.write_videofile("Python表达式1.mp4")


'''19.2.3实现视频转码'''
# from moviepy.editor import VideoFileClip
# clip = VideoFileClip("Python表达式.mp4",).subclip(100,120)
# clip.write_videofile("Python表达式1.avi",codec= 'rawvideo',logger = None)


'''19.2.3将整个文件夹中的视频文件全部转码为'''
# from moviepy.editor import VideoFileClip
# import os
# for file_name in os.listdir('./视频转码'):
#     ex_file_name = './视频转码/' + file_name  #字符串连接
#     ex_file_name_new = ex_file_name.replace('mp4','avi')
#     print(ex_file_name_new)
#     clip = VideoFileClip(ex_file_name)
#     clip.write_videofile(ex_file_name_new,codec= 'png' ,logger = None)




'''19.2.4视频的串联'''
# from moviepy.editor import VideoFileClip,concatenate_videoclips
# clip1 = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip2 = VideoFileClip("Python语言的发展经历.mp4").subclip(100,120)
# clip3 = VideoFileClip("Python考试介绍.mp4").subclip(100,120)
# clip_all = concatenate_videoclips([clip1,clip2,clip3])
# clip_all.write_videofile("Python表达式1.mp4")


'''19.2.4实现视频串联，且带有转场及淡入效果'''
# from moviepy.editor import VideoFileClip,concatenate_videoclips
# clip1 = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip2 = VideoFileClip("Python语言的发展经历.mp4").subclip(100,120)
# clip3 = VideoFileClip("Python考试介绍.mp4").subclip(100,120)
# clip4 = VideoFileClip("转场.mp4")
# clip_all = concatenate_videoclips([clip1,clip2,clip3],method='compose', transition=clip4, padding = -1)
# clip_all.write_videofile("Python表达式2.mp4")



'''19.2.4使用多次concatenate_videoclips串联实现指定区域增加转场'''
# from moviepy.editor import VideoFileClip,concatenate_videoclips
# clip1 = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip2 = VideoFileClip("Python语言的发展经历.mp4").subclip(200,230)
# clip3 = VideoFileClip("Python考试介绍.mp4").subclip(50,130)
# clip4 = VideoFileClip("转场.mp4")
# clip12 = concatenate_videoclips([clip1,clip2],method='compose', transition=clip4, padding = -0.5)
# clip_all = concatenate_videoclips([clip12,clip3])
# clip_all.write_videofile("Python表达式2.mp4")



'''19.2.5'''
# from moviepy.editor import VideoFileClip
# clip1 = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip1.save_frame("视频帧.png",t=10)



# from moviepy.editor import VideoFileClip
# clip1 = VideoFileClip("Python表达式.mp4").subclip(100,110)
# clip1.write_images_sequence('some_folder/frame%04d.jpeg',fps = 5 ,logger=None)



# from moviepy.editor import VideoFileClip
# clip1 = VideoFileClip("转场.mp4")
# clip1.write_gif('转场.gif',fps = 1)





'''19.2.6'''
# from moviepy.editor import VideoFileClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# clip1 =clip.resize(width=480)
# clip2 = clip.resize(0.5)
# clip3 = clip.resize(height = 480)
# clip1.write_videofile("Python表达式1.mp4")
# clip2.write_videofile("Python表达式2.mp4")
# clip3.write_videofile("Python表达式3.mp4")


'''19.2.7'''
# from moviepy.editor import VideoFileClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip.show(11)
# clip.preview()


'''19.2.8'''
# from moviepy.editor import VideoFileClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110).margin(10)
# clip1 = clip.resize(0.7).set_position((0.4,0.7))
# clip2 = clip.resize(width=780).set_position(("center","top"))
# clip_all = CompositeVideoClip([clip,clip1,clip2])
# clip_all.write_videofile("Python表达式1.mp4")

'''19.2.8*****'''
# from moviepy.editor import VideoFileClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# clip1 = VideoFileClip("Python考试介绍.mp4").subclip(100,110).resize(0.7).set_position((0.4,0.7), relative=True)
# clip2 = VideoFileClip("转场.mp4").resize(width=780).set_position(("center","top")).margin(10)
# clip_all = CompositeVideoClip([clip,clip1,clip2])
# clip_all.write_videofile("组合播放.mp4")
#margin方法设置剪辑对象的边框，其中参数为边框的宽度，单位为像素。


'''19.2.8*****画面在视频窗口中移动的效果'''
# from moviepy.editor import VideoFileClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# clip1 = VideoFileClip("转场.mp4").resize(width=780).set_position(lambda t: (100+20*t, 100+20*t))
# clip_all = CompositeVideoClip([clip,clip1])                             #(120,120)(140,140)
# clip_all.write_videofile("Python表达式1.mp4")




# from moviepy.editor import VideoFileClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110).margin(10)
# clip1 = clip.resize(0.7).set_position((0.3,0.3),relative= True)
# clip2 = clip.resize(width=780).set_position(lambda t: ('center', 100+20*t))
# clip_all = CompositeVideoClip([clip,clip1,clip2])
# clip_all.write_videofile("Python表达式1.mp4")



'''19.2.9'''
# from moviepy.editor import VideoFileClip
# clip1 = VideoFileClip("Python表达式.mp4").subclip(0,5)
# clip1 = clip1.on_color(size=(1920,3500),color=(240,248,255),col_opacity=0.8)
# clip1.write_videofile("Python表达式2.mp4")



'''19.3.1'''
# from moviepy.editor import ImageClip,concatenate_videoclips
# img1 = ImageClip('聪明的投资者.jpg',duration=5)
# img2 = ImageClip('极简主义.jpg',duration=5)
# img3 = ImageClip('善用时间.jpg',duration=5)
# clip_all = concatenate_videoclips([img1,img2,img3])
# clip_all.write_videofile("Python表达式2.avi",fps =1,codec= 'png')




# from moviepy.editor import ImageClip,concatenate_videoclips,VideoFileClip
# clip1 = VideoFileClip("Python表达式.mp4").subclip(0,5)
# img1 = ImageClip('聪明的投资者.jpg',duration=5)
# clip_all = concatenate_videoclips([clip1,img1])
# clip_all.write_videofile("Python表达式2.mp4",codec= 'libx264')


'''19.3.2添加logo'''
# from moviepy.editor import VideoFileClip,ImageClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,120)
# logo = ImageClip('Python图标.png',duration=clip.duration) # logo持续时间
# logo = logo.set_position((10, 10))  # logo的位置
# logo = logo.resize(width = 150)
# clip_all = CompositeVideoClip([clip,logo])
# clip_all.write_videofile("Python表达式1.mp4")



'''19.3.2添加动态logo'''
# from moviepy.editor import VideoFileClip,ImageClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,120)
# logo = ImageClip('Python图标.png',duration=clip.duration) # logo持续时间
# logo = logo.resize(width = 150).set_position(lambda t: (96*t, 54*t))
# clip_all = CompositeVideoClip([clip,logo]) #96，54，
# clip_all.write_videofile("Python表达式1.mp4")


'''19.3.3批量生成视频水印'''
# import os
# from moviepy.editor import VideoFileClip , ImageClip, CompositeVideoClip
# for file_name in os.listdir('./视频'):
#     file_adr = './视频/' + file_name
#     file_new_adr = './视频水印/' + file_name
#     clip = VideoFileClip(file_adr)
#     logo = ImageClip('水印图标.png',duration=clip.duration)
#     logo = logo.resize(width = 150).set_pos((10, 10))
#     clip_all = CompositeVideoClip([clip,logo])
#     clip_all.write_videofile(file_new_adr)


'''19.4.1'''
# from moviepy.editor import AudioFileClip
# audioclip1 = AudioFileClip("一千年以后.mp3")
# audioclip2 = AudioFileClip("Python表达式.mp4")
# audioclip1.preview()
# audioclip2.preview()



'''19.4.1导出视频中的音频*****'''
# from moviepy.editor import AudioFileClip
# audioclip2 = AudioFileClip("Python表达式.mp4")
# audioclip2.write_audiofile('Python表达式.mp3')



'''19.4.2设置视频的音频    替换视频中的声音'''
# from moviepy.editor import VideoFileClip,AudioFileClip
# audioclip1 = AudioFileClip("一千年以后.mp3").subclip(0,20)
# clip2 = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip2 = clip2.set_audio(audioclip1)
# clip2.write_videofile("Python表达式1.mp4")

'''19.4.2删除视频的音频'''
# from moviepy.editor import VideoFileClip
# clip2 = VideoFileClip("Python表达式.mp4").subclip(100,120).without_audio()
# clip2.write_videofile("Python表达式1.mp4")



'''19.4.3设置音量volumex'''
# from moviepy.editor import AudioFileClip,VideoFileClip
# audioclip1 = AudioFileClip("一千年以后.mp3").subclip(0,20).volumex(0.1)
# clip2 = VideoFileClip("Python表达式.mp4").subclip(100,120)
# clip2 = clip2.set_audio(audioclip1)
# clip2.write_videofile("Python表达式1.mp4")





'''19.5.1'''
# from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# txtClip= TextClip(txt='Python learning', fontsize=100,color='white',bg_color = 'black',font="Castellar",kerning = 5)
# # print(txtClip.list('color'))
# txtClip = txtClip.set_position((200,210)).set_duration(10)
# clip_all = CompositeVideoClip([clip,txtClip])
# clip_all.write_videofile("Python表达式1.mp4")



# from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# txtClip= TextClip(txt='Python learning',fontsize=100,color='white',bg_color='black',font="BELLB.TTF",kerning = 5)
# txtClip = txtClip.set_position((200,210)).set_start(t='00:00:01.850' ,change_end=False).set_end(t='00:00:03.680')
# clip_all = CompositeVideoClip([clip,txtClip])
# clip_all.write_videofile("Python表达式1.mp4")



'''实现中文字幕'''
# from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# txtClip= TextClip(txt='大家好，我正在学习Python', fontsize=100,color='white',bg_color = 'black',font="simhei.ttf",kerning = 5)
# txtClip = txtClip.set_position((200,210)).set_duration(10)
# clip_all = CompositeVideoClip([clip,txtClip])
# clip_all.write_videofile("Python表达式2.mp4")



'''19.5.2滚动文字'''
# from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip
# clip = VideoFileClip("Python表达式.mp4").subclip(100,110)
# txtClip= TextClip(txt='Python learning',fontsize=50,color='white',kerning = 5)
# txtClip = txtClip.set_start(t='00:00:01.150' ,change_end=False).set_end(t='00:00:07.980')
# txtClip = txtClip.set_position(lambda t: (1920-300*t, 100))
# clip_all = CompositeVideoClip([clip,txtClip])
# clip_all.write_videofile("Python表达式1.mp4")



'''19.6项目：实现自动添加字幕'''
from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip
clip = VideoFileClip("Python表达式.mp4").subclip(0,10)
textclip_list = []#存储每一个文本剪辑对象
text = open('程序的语句.srt','r',encoding='utf-8')
d = text.readlines()
num = len(d)//4  #确定字幕的内容个数，一个字幕内容包含标号、时间、内容、空行共4行
for i in range(num):
    time = d[i*4+1].replace(',','.').strip('\n').split(' -->') #字幕的时间处理，利于后期处理
    print(time)
    line_text = d[i*4+2].strip('\n')#字幕的内容
    print(line_text)
    textclip = TextClip(txt=line_text, fontsize=50, color='white', font="simhei.ttf", kerning=5)
    textclip = textclip.set_position(('center',990)).set_start(t=time[0] ,change_end=False).set_end(t=time[1])
    textclip_list.append(textclip)
clip_all = CompositeVideoClip([clip]+textclip_list)
clip_all.write_videofile("Python表达式3字幕.mp4")
text.close()











