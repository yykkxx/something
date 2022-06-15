import psutil
import time
import tkinter
import threading
import math
t=tkinter.Tk()
t.title("")
t.geometry("140x100")
t.resizable(0,0)
def cpu():
    return psutil.cpu_count(),psutil.cpu_count(logical=False),psutil.cpu_freq().current
def svmem_total():
    mem = psutil.virtual_memory()
    return mem.total
def svmem():
    mem = psutil.virtual_memory()
    return mem.free,mem.used
def get_cpu():
    psutil.cpu_percent()
    time.sleep(0.3)
    return psutil.cpu_percent()+2
count,count_l,current = cpu()
if count >= count_l:
    count = "核心数:"+str(count)+" thread"
    count_l = "线程数:"+str(count_l)+" core"
    tkinter.Label(t,text=count_l).pack()
    tkinter.Label(t,text=count).pack()
else:
    count_l = "线程数:"+str(count_l)+" thread"
    count = "核心数:"+str(count)+" core"
    tkinter.Label(t,text=count).pack()
    tkinter.Label(t,text=count_l).pack()
current = "主频:"+str(current)+" MHz"
total = "内存:"+str(math.floor(svmem_total()/1024/1024))+" MB"
tkinter.Label(t,text=current).pack()
tkinter.Label(t,text=total).pack()
t.mainloop()
