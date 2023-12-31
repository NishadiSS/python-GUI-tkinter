import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Slider')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

scale = ttk.Scale(root, command=lambda value:print(value), from_=0,to=50,length=300,orient='horizontal',value=30)
scale.pack()

root.mainloop()
