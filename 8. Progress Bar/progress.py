import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('progress bar')
root.iconbitmap('icon.ico')
root.geometry('300x200')

progress_bar= ttk.Progressbar(root,length=200,value=50,orient='horizontal')
progress_bar.pack()

root.mainloop()