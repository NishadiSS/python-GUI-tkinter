import tkinter as tk 
from tkinter import ttk 

root=tk.Tk()

root.title("Tree View")
root.iconbitmap("icon.ico")
root.geometry('700x400')
root.resizable(False,False)

table=ttk.Treeview(root,columns=('id','name','gender','salary'),show='headings')
table.heading('id',text='Id')
table.heading('name',text='Name')
table.heading('gender',text='Gender')
table.heading('salary',text='Salary')

table.column('id',width=100)
table.pack()

id=[1,2,3,4,5,6,7,8,9,10]
name =['Mark','John','Pam','Sara','Todd','Mary','Ben','Jodi','Tom','Ron']
gender = ['Male','Male','Female','Female','Male','Female','Male','Female','Male','Male']
salary =[8000,8000,5000,4000,3500,6000,6500,4500,7000,6800]

def selected_item(event):
    print(table.item(table.selection())['values'])

for idx,value in enumerate(name):
    table.insert('',idx,values=(id[idx],name[idx],gender[idx],salary[idx]))

table.bind('<<TreeviewSelect>>',lambda event:selected_item(event))

#table.insert('',0,values=(1,'Mark','Male',8000))
#table.insert('',0,values=(2,'John','Male',8000))




root.mainloop()