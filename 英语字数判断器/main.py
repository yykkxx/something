file = open("简历.txt")
txt = file.read()
file.close()
index = 0
import tkinter
t = tkinter.Tk()
t.resizable(0,0)
t.geometry("100x50")
for x in range(len(txt)):
    i = txt[x]
    print(i)
    if txt[x] == " " or "," or "." or "!" or "?":
        index += 1
index = "写了" + str(index) + "词"
tkinter.Label(t,text=index).pack()
t.mainloop()
