from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time

root = Tk()
root.geometry("1500x1800")
canvas = Canvas(root,width=1500, height=1800,bg='white')
canvas.pack()
img=[]

#分解gif并逐帧显示
def pick(event):
    global a,flag   
    while 1:
        im = Image.open('lion.gif')
        # GIF图片流的迭代器
        iter = ImageSequence.Iterator(im)
        #frame就是gif的每一帧，转换一下格式就能显示了
        for frame in iter:
            pic=ImageTk.PhotoImage(frame)
            canvas.create_image((800,850), image=pic)
            time.sleep(0.1)
            root.update_idletasks()  #刷新
            root.update()

canvas.bind("<Enter>",pick)  #这个事件是鼠标进入组件，用什么事件不重要，这里只是演示
root.mainloop()