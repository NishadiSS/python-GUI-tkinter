import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()

root.title('Toggle')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

bulb_state=tk.BooleanVar(value=False)

def change_state():
    if bulb_state.get():
        bulb_state.set(False)
        bulb.configure(text='OFF')
    else:
        bulb_state.set(True)
        bulb.configure(text='ON')
    print(bulb_state.get())

switch = ttk.Button(root,text='Switch',command=change_state)
switch.pack(side='bottom',pady=20)

bulb = ttk.Label(text='OFF')
bulb.place(relx=0.5,rely=0.5)


root.mainloop()