import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox 

root= tk.Tk()
root.title("Message boxes")
root.iconbitmap("icon.ico")
root.geometry("500x400")

def open_messagebox():
     result =messagebox.askokcancel("This is a title", "This is a message")
     print(result)

button = ttk.Button(root,text='Click Me',command=open_messagebox)
button.pack()

root.mainloop()