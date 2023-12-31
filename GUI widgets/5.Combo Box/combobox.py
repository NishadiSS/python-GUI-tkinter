import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()

root.title('ComboBox')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

month_names = [month_name[i] for i in range(1,13)]

combobox= ttk.Combobox(root, values=month_names)
combobox.pack()

root.mainloop()