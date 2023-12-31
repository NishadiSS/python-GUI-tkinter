import tkinter as tk 
from tkinter import ttk
from calendar import month_name

root = tk.Tk()

root.title('spinbox')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

month_names = [month_name[i] for i in range(1,13)]

spinbox = ttk.Spinbox(root,values = month_names)
spinbox.pack()

root.mainloop()