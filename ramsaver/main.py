import tkinter as tk
import psutil
import time as te
import threading
def getram():
    mem = psutil.virtual_memory()
    return int(mem.total/1000/1000/1000)
def save():
    g = 1024 * 1024 * 256/2.2
    g = int(g)
    data = "a" * g
    te.sleep(2)
def save_t(time):
    for x in range(time):
        threading.Thread(target=save).start()
        print("sb")
t=tk.Tk()
t.title("ram")
t.resizable(0,0)
tk.Label(t,text = "            这是一个内存占用器            \n会消耗你的内存\n点击任意按键就可以占用1GB内存\n不是按钮上面的").pack()
times = getram()
index = 1
while times >= index:
    text = "     " + str(index) + "GB" + "     "
    tk.Button(t,text = text,command = lambda:save_t(index)).pack()
    index += 1
t.mainloop()
