import tkinter as tk

root = tk.Tk()

root.title('Form')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

radio_var = tk.StringVar()

label5 = tk.Label(root, text = "Gender",font="time 12 bold")
label5.pack()

radio1 = tk.Radiobutton(root,text='Male',value='Male',variable=radio_var,font="time 10")
radio1.pack()

radio2 = tk.Radiobutton(root,text='Female',value='Female',variable=radio_var,font="time 10")
radio2.pack()

root.mainloop()