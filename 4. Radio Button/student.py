import tkinter as tk

root = tk.Tk()

root.title('Form')
root.iconbitmap('icon.ico')
root.geometry('300x200')
root.resizable(False,False)

label5 = tk.Label(root, text = "Gender",font="time 12 bold")
label5.pack()

radio1 = tk.Radiobutton(root,text='Male',value='Male',font="time 10")
radio1.pack()

radio2 = tk.Radiobutton(root,text='Female',value='Female',font="time 10")
radio2.pack()

root.mainloop()