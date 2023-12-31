import tkinter as tk
#from tkinter import ttk

# create a window
root = tk.Tk()

root.title("Basic Widgets")
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False) #cannot resize

#initialize button
#old_button = tk.Button(root,text='Click Me')
#pack button in the window
#old_button.pack()

def button_click_func():
    entry_field_value = entry.get()
    label.configure(text=entry_field_value)

    #After clicking the button once, to disable button
    button.configure(state='disabled')

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Click Me',command=button_click_func)  #command=button_click_func() magin run weddima hello print wenawa.
button.pack()

label = tk.Label(root)
label.pack()


# run the window
root.mainloop()

