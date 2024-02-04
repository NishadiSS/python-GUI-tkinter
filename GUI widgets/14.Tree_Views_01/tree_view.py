import tkinter as tk 
from tkinter import ttk

root=tk.Tk()

root.title("Tree_View")
root.iconbitmap("icon.ico")
root.geometry('500x400')
root.resizable(False,False)

table=ttk.Treeview(root, columns=('name','age','email'), show='headings')
table.heading('name',text='Name')
table.heading('age',text='Age')
table.heading('email',text='Email')
table.column('age',width=100)
table.pack()

name = ['kamal','saman','pawan','gayan']
age = [34,53,32,54]

def selected_item(event):
    print(table.item(table.selection())['values'])

#table.insert('',0,values=('kamal',20,'kamal@gmail.com'))
#table.insert('',1,values=('saman',26,'saman@gmail.com'))

for idx,value in enumerate(name):
    table.insert('',idx,values=(name[idx],age[idx],f'{name[idx]}@gmail.com'))

table.bind('<<TreeviewSelect>>',lambda event:selected_item(event))

root.mainloop()

