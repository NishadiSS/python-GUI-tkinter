import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Canvas')
root.geometry('500x400')
root.iconbitmap('icon.ico')
root.resizable(False,False)

canvas = tk.Canvas(root ,bg='white')
canvas.pack()

brush_width = 2

def draw(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='black')

def start_drawing(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='black')
    canvas.bind('<B1-Motion>',draw)


canvas.bind('<Button-1>',start_drawing)

root.mainloop()