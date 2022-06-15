import tkinter
from tkinter.filedialog import *
import os
t=tkinter.Tk()
t.resizable(0,0)
t.geometry("350x60")
t.title("genshin impact start plus")
f=open("config.ini",mode="r")
index=f.read()
f.close()
if len(index)==0:
    path=askopenfilename()
    f=open("config.ini",mode="w")
    f.write(path)
    f.close()
f=open("config.ini",mode="r")
index=f.read()
print(index)
f.close()
index="\""+index+"\""
print(index)
def start(index):
    os.popen(index)
def again():
    path=askopenfilename()
    f=open("config.ini",mode="w")
    f.write(path)
    f.close()
tkinter.Button(t,text="start",command=lambda:start(index)).pack()
tkinter.Button(t,text="again",command=again).pack()
t.mainloop()
