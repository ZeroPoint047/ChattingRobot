import shibie
import luyin
import requests, json, time, random
from playsound import playsound
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time
from threading import Thread
#flag为1时，小狮子嘴巴动起来
flag=1
#语音路径 自定义
path=r'C:\Users\zhuqian\Desktop\s\myword.mp3'
def asyn(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper
#录音时开启一个线程防止卡死
@asyn
def chatting():
    
    #录音
    luyin.rec(path)
    #语音识别
    text=shibie.identify(path)
    print(text)

    userid = str(random.randint(1, 1000000000000000000000))
    apikey = 'ef9722561c97454e9c5d661f0fb9aac1'
            
    tulingdata1 = json.dumps({
                "perception": {
                "inputText": {
                    "text": text
                },

            },
                "userInfo": {
                    "apiKey": apikey,
                    "userId": userid
                }
    })
    robot1 = requests.post('http://openapi.tuling123.com/openapi/api/v2', tulingdata1)
    jsrobot1 = json.loads(robot1.text)['results'][0]['values']['voice']
    jsrobot2 = json.loads(robot1.text)['results'][1]['values']['text']
    print(jsrobot2)
    playsound(jsrobot1)
    global flag
    flag=0
    print(flag)
    time.sleep(2)


# def bizui():
#     global image,pic,canvas,root,flag
#     flag=0
#     image = Image.open("2.jpg")
#     pic=ImageTk.PhotoImage(image)
#     canvas.create_image((800,850), image=pic)
#     root.update_idletasks()  #刷新
#     root.update()
            

#点击说话
'''
点击按钮时的操作：
'''
def test():
    B.configure(state=DISABLED) #按钮变灰色
    global flag
    flag=1
    
    chatting()  #开始聊天
    pick(1)     #图片开始动
    B.configure(state="normal") #对话结束，按钮恢复

#分解gif并逐帧显示

def pick(event):
    global image,pic,canvas,root,flag
    
    while flag:
        
        im = Image.open('lion.gif')
        # GIF图片流的迭代器
        iter = ImageSequence.Iterator(im)
        #frame就是gif的每一帧，转换一下格式就能显示了
        for frame in iter:
            pic=ImageTk.PhotoImage(frame)
            canvas.create_image((600,500), image=pic)
            time.sleep(0.1)
            root.update_idletasks()  #刷新
            root.update()
root = Tk()
root.geometry("1250x1618")
B = Button(text ="点击说话" ,command=test)
B.pack()

canvas = Canvas(root,width=1200, height=1200,bg='white')
canvas.pack()
image = Image.open("2.jpg")  
pic=ImageTk.PhotoImage(image)
canvas.create_image((600,500), image=pic)


        
#canvas.bind("<1>",pick)  #这个事件是鼠标进入组件，用什么事件不重要，这里只是演示
           
root.mainloop()
