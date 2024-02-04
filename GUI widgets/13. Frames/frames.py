import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.title("Frames")
root.geometry("500x400")
root.iconbitmap("icon.ico")
root.resizable(False,False)

frame1 =ttk.Frame(root,width=200,height=200,relief = tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack(side="bottom")

entry1 = ttk.Entry(frame1)
entry1.pack(pady=10)

button1=ttk.Button(frame1,text="Submit")
button1.pack()

frame2 = ttk.Frame(root,width=400,height=100,relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack()

label1 = ttk.Label(frame2,text="Welcome to CodeNish Design channel")
label1.pack(pady=20)

button2=ttk.Button(frame2,text="OK")
button2.pack()



root.mainloop()