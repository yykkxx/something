import tkinter as tk
from tkinter import ttk
import os
import _thread
t=tk.Tk()
t.geometry("800x320")
t.title("wifi tester")
t.resizable(0,0)
photo=tk.PhotoImage(file="wifi.png")
tk.Label(t,image=photo).place(x=0,y=0,anchor="nw")
tk.Label(t,text="请等待一会,大约十秒钟").place(x=300,y=23,anchor="nw")
cmb = ttk.Combobox(t)
cmb['value'] = ('speedtest','ping')
cmb.current(0)
cmb.place(x=73,y=25,anchor="nw")
def run(t,cmb):
    p= ttk.Progressbar(t, length=200, mode="indeterminate",maximum=200,orient=tk.HORIZONTAL)
    p.place(x=450,y=23,anchor="nw")
    p.start()
    _thread.start_new_thread(start,(t,cmb,p,))
def start(t,cmb,p):
    if cmb.get()=='speedtest':
        f=os.popen('.\Python38\python.exe speedtest.py').read()
        tk.Label(t,text="data").place(x=10,y=75,anchor="nw")
        tk.Label(t,text=f).place(x=10,y=100,anchor="nw")
    if cmb.get()=='ping':
        f=os.popen('ping www.baidu.com').read()
        tk.Label(t,text="data").place(x=10,y=75,anchor="nw")
        tk.Label(t,text=f).place(x=10,y=100,anchor="nw")
    p.destroy()
b=tk.Button(t,command=lambda:run(t,cmb),text="start").place(x=250,y=20,anchor="nw")
t.mainloop()

