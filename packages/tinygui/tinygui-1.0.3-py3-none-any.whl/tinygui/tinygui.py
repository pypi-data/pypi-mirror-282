import tkinter as tk
import pygame
from tkinter.ttk import *
from tkinter import*
from PIL import Image, ImageTk
from time import time
from qrcode import make
import threading
from functools import partial

pwd = ''
root = ''
def tk_init(txt=''):
    global pwd,root
    pwd = ''
    root = tk.Tk()
    # 创建一个Label组件
    label = tk.Label(root,text=txt,bg='white')
    #root.iconphoto(False,'pwd.png')
    root.title('')
    label.pack()
    root.geometry("300x120+500+140")
    root.resizable(width=False, height=False)
    root.configure(bg='white')

def input_text(txt=''):
    tk_init(txt)
    def get_pwd():
       global pwd
       pwd = password_entry.get()
       #root.destroy()
       #print(pwd)
       root.destroy()
       #return pwd
    def on_close():
        global pwd
        pwd = ''
        root.destroy()

    password_entry = tk.Entry(root, show="",bd=5,width=35)
    password_entry.pack()
    ensureButton = Button(root, text ="确定", command = get_pwd)
    ensureButton.pack(padx = 25,ipadx=10,side='left')
    cancleButton = Button(root,text='取消',command=on_close)
    cancleButton.pack(padx = 25,ipadx=10,side='right')
    # 创建一个Entry组件，设置显示形式为星号
    # 运行主循环
    try:
        mainloop()
    except:
        pass
    return str(pwd)

def get_value():
    return str(pwd)

# pygame窗口显示文本方法
def draw_text(screen, text, pos, mark=0):
    # 设置文本框的外观
    text_box_rect = pygame.Rect(pos, (100, 40))
    text_layer = pygame.Surface(pos, pygame.SRCALPHA)
    text_layer.fill((255, 255, 255, 0))
    screen.blit(text_layer, pos)
    font = pygame.font.Font(None, 55)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=text_box_rect.center)
    screen.blit(text_surface, text_rect)
    pygame.display.update()

# tk创建窗口方法
def create_win(title, size):
    # 创建显示窗口
    win = tk.Tk()
    # 设置窗口标题
    win.title(title)
    # 设置窗口大小
    win.geometry('{}x{}'.format(size[0], size[1]))
    # 规定窗口不可缩放
    win.resizable(False, False)
    return win


def set_photo(path,win):
    image = Image.open(path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(win,image=photo)
    label.image = photo
    label.place(x=0, y=0)

def create_root(size=(600,400), title='小河狸程序',  path=''):
    # 创建显示窗口
    global win
    win = tk.Tk()
    # 设置窗口标题
    win.title(title)
    # 设置窗口大小
    win.geometry('{}x{}'.format(size[0], size[1]))
    # 规定窗口不可缩放
    win.resizable(False, False)
    if path:
        set_photo(path, win)
    return win

def create_sub(root, size=(600,400), title='小河狸程序',  path=''):
    # 设置所属主窗口
    new_window =  tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry('{}x{}'.format(size[0], size[1]))
    # 规定窗口不可缩放
    new_window.resizable(False, False)
    if path:
        set_photo(path, new_window)
    return new_window


#  tk创建标签方法
def create_label(window=None, pos=None, size=(100,40), text='标签',  bg='yellow', anchor='center', fz=12):
    global id
    if window:
        lb = myLabel(window,  bg=bg, font=('msyhbd.ttc', fz, 'bold'), text=text, anchor=anchor)
    else:
        lb = myLabel(win,  bg=bg,  font=('msyhbd.ttc', fz, 'bold'), text=text, anchor=anchor)
    if pos == None:
        pos = (id*100, 0)
        id += 1 
    lb.place(x=pos[0], y=pos[1], width=size[0], height=size[1])
    return lb

# tk创建按钮方法
def create_button( window=None, pos=None, size=(100,40), text='按钮', fz=14):
    global id
    if window:
        btn = tk.Button(window, text=text, font=('msyhbd.ttc', fz, 'bold'))
    else:
        btn = tk.Button(win, text=text, font=('msyhbd.ttc', fz, 'bold'))
    if pos == None:
        pos = (id*100, 0)
        id += 1
    btn.place(x=pos[0], y=pos[1], width=size[0], height=size[1])
    return btn

# tk创建输入框方法
def create_entry(win, pos, size, text='',  fz=18):
    string = tk.StringVar()
    ety = tk.Entry(win, text=text, font=('msyh.ttc', fz), textvariable=string)
    ety.place(x=pos[0], y=pos[1], width=size[0], height=size[1])
    return ety

def generate_qrcode():
    global new_window
    
    new_window = tk.Toplevel()
    new_window.title("付款码")
    
    info = 'finished'
    qr_code_image = ImageTk.PhotoImage(make(info))
    qr_code_label = tk.Label(new_window, image=qr_code_image)
    qr_code_label.image = qr_code_image  # 保持引用，防止被垃圾回收
    qr_code_label.pack(pady=10)

def close_qrcode():
    new_window.destroy()
    
def show_control(control,pos):
    #confirm.place(x = 170, y = 400)
    control.place(x=pos[0],y=pos[1])

def unshow_control(control):
    control.place_forget()

