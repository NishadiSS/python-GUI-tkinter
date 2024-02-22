import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title("Calculator")
root.iconbitmap("icon.ico")
root.resizable(False,False)

frame1 = ttk.Frame(root)
frame1.pack(pady=10, padx=10)

entry1 = ttk.Entry(frame1)
entry1.pack(pady=10,padx=10,side='left')

entry2 = ttk.Entry(frame1)
entry2.pack(pady=10,padx=10,side='right')

frame2 = ttk.Frame(root)
frame2.pack(side="bottom",pady=10)

def Fun1():
    x=entry1.get()
    y=entry2.get()
    z=int(x) + int(y)

    label1.config(text=str(z))

def Fun2():
    x=entry1.get()
    y=entry2.get()
    z=int(x) - int(y)

    label1.config(text=str(z))

def Fun3():
    x=entry1.get()
    y=entry2.get()
    z=int(x) / int(y)

    label1.config(text=str(z))

def Fun4():
    x=entry1.get()
    y=entry2.get()
    z=int(x) * int(y)

    label1.config(text=str(z))

button1= ttk.Button(frame2,text="+",command=Fun1)
button1.pack(side="left")

button2= ttk.Button(frame2,text="-",command=Fun2)
button2.pack(side="left")

button3= ttk.Button(frame2,text="/",command=Fun3)
button3.pack(side="left")

button4= ttk.Button(frame2,text="*",command=Fun4)
button4.pack(side="left")

label1=ttk.Label(root,text="0")
label1.pack()

root.mainloop()