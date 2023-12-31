import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Events')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

button= ttk.Button(root,text='OK')
button.pack()

#root.bind('<key>',lambda event:print('welcome'))
#button.bind('<Key>',lambda event:print('welcome'))

button.bind('<Enter>',lambda event:print('Enter to button'))
button.bind('<Leave>',lambda event:print('Leave from button'))

root.mainloop()