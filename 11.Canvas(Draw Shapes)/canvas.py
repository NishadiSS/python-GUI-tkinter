import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('canvas')
root.iconbitmap('icon.ico')
root.geometry('500x400')
root.resizable(False,False)

canvas = tk.Canvas(root,bg='white')
canvas.pack()

canvas.create_rectangle((20,20,100,100), fill='blue')
canvas.create_oval((100,100,200,250),fill='green')
canvas.create_polygon((255,25,260,155,300,100),fill='red')
canvas.create_line((0,0,255,255), fill='yellow',width=5)

root.mainloop()