'''
小狮子讲话
'''

def helloCallBack():
    chat.chatting()
import chat       
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import time

root = Tk()
root.title('乐程小狮子')
root.geometry('1500x1800')
root.geometry('+1000+100')

bm = ImageTk.PhotoImage(file='lion.gif')
label = Label(root, image=bm)
label.bm = bm

B = Button(text ="点击说话", command = helloCallBack)
B.pack()
label.pack()

# 进入消息循环
root.mainloop()
