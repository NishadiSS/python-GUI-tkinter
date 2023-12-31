import tkinter as tk

root = tk.Tk()

root.title('Form')
root.iconbitmap('icon.ico')
root.geometry('400x400')
root.resizable(False,False)

radio_var = tk.StringVar()

def button_click_func():
    button.configure(state='disabled')


label1 = tk.Label(root, text = "Student Registration",font="time 18 bold ",background="pink")
label1.pack()

label2 = tk.Label(root, text = "First Name",font="time 12 bold")
label2.pack()

entry1 = tk.Entry(root,width=50,bd=5)
entry1.pack()

label3 = tk.Label(root, text = "Last Name",font="time 12 bold")
label3.pack()

entry2 = tk.Entry(root,width=50,bd=5)
entry2.pack()

label4 = tk.Label(root, text = "Email",font="time 12 bold")
label4.pack()

entry3 = tk.Entry(root,width=50,bd=5)
entry3.pack()

label5 = tk.Label(root, text = "Gender",font="time 12 bold")
label5.pack()

radio1 = tk.Radiobutton(root,text='Male',value='Male',variable=radio_var,font="time 10")
radio1.pack()

radio2 = tk.Radiobutton(root,text='Female',value='Female',variable=radio_var,font="time 10")
radio2.pack()

button=tk.Button(root,text="Submit",command=button_click_func,width=10,height=1,background="red",font="time 15 bold")
button.pack()
root.mainloop()