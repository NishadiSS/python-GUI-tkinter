import tkinter as tk 
from tkinter import ttk

root=tk.Tk()
root.title("Layouts")
root.iconbitmap("icon.ico")
root.geometry("500x400")

hello_label=ttk.Label(root,text='Hello',background='pink')
codenish_label=ttk.Label(root,text='CodeNish',background='yellow')

#hello_label.pack()
#codenish_label.pack(side='left',expand=True,fill='both')

# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=1)
# root.columnconfigure(2,weight=1)
# root.rowconfigure(0,weight=1)
# root.rowconfigure(1,weight=1)

# hello_label.grid(row=1,column=1,sticky='nsew')
# codenish_label.grid(row=0,column=2,sticky='nsew')

hello_label.place(x=400,y=100,width=100,height=100)
codenish_label.place(relx=0.5,rely=0.5,width=100,height=100)


root.mainloop()