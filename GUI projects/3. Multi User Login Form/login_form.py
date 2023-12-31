import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Login Form For Multiple Users')
root.iconbitmap('icon.ico')
root.geometry('400x300')
root.resizable(False,False)

label1 = tk.Label(root,text = 'Username',font='time 12 bold')
label1.pack()

entry1 = tk.Entry(root,width=50,bd=5)
entry1.pack()

label2 = tk.Label(root,text = 'Email',font='time 12 bold')
label2.pack()

entry2 = tk.Entry(root,width=50,bd=5)
entry2.pack()

label3 = tk.Label(root,text = 'Select User Type',font='time 12 bold')
label3.pack()

combobox = ttk.Combobox(root,values=['admin','user'])
combobox.pack()

button = tk.Button(root,text="Login",width=10,background='yellow',font="time 12 bold")
button.pack()
button.place(relx=0.5,rely=0.65,anchor=tk.CENTER)

root.mainloop()