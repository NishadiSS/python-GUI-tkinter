import tkinter as tk 
root = tk.Tk()
root.title("Menu")
root.iconbitmap("icon.ico")
root.geometry("500x400")

menu = tk.Menu(root)

file_menu = tk.Menu(menu,tearoff=False)
file_menu.add_command(label='New', command=lambda:print("New"))
file_menu.add_command(label='Open',command=lambda:print("Open"))
file_menu.add_command(label='Save',command=lambda:print("Save"))
file_menu.add_command(label='Save as',command=lambda:print("Save as"))
file_menu.add_command(label='Exit',command=lambda:print("Exit"))
menu.add_cascade(label='File',menu=file_menu)

edit_menu = tk.Menu(menu)
edit_menu.add_command(label='Undo')
edit_menu.add_checkbutton(label='Cut')
menu.add_cascade(label='Edit',menu=edit_menu)

root.configure(menu=menu)
root.mainloop()