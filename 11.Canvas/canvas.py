import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('canvas')
root.iconbitmap('icon.ico')
root.geometry('500x400')
root.resizable(False,False)

canvas = tk.Canvas(root,bg='white')
canvas.pack()

brush_width=2

def draw(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='black')

def start_drawing(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brush_width,y-brush_width,x+brush_width,y+brush_width),fill='black')
    canvas.bind('<B1-Motion>',draw)

#canvas.create_rectangle((20,20,100,100), fill='blue')
#canvas.create_oval((100,100,200,250),fill='green')
#canvas.create_polygon((255,25,260,155,300,100),fill='red')
#canvas.create_line((0,0,255,255), fill='yellow',width=5)

canvas.bind('<Button-1>',start_drawing)
#canvas.bind('<Motion>',draw)

root.mainloop()