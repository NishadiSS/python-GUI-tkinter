import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Slider with Progress Bar')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

scale_value = tk.DoubleVar(value=50)

scale = ttk.Scale(root,length=200,variable=scale_value,from_=0,to=100)
scale.pack()

progressbar= ttk.Progressbar(root,length=200,variable=scale_value)
progressbar.pack()
root.mainloop()