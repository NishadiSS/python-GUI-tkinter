import tkinter as tk

root = tk.Tk()
root.title('Check Box')
root.iconbitmap('icon.ico')
root.geometry('600x300')

label_var = tk.StringVar()
check1_var = tk.StringVar()
check2_var = tk.StringVar()

def checkbox_results():
    output_string = "Selected Skills: "+check1_var.get()+' '+check2_var.get()
    label_var.set(output_string)
    print(check1_var.get())
    print(check2_var.get())

check1 = tk.Checkbutton(root,text='Web application development',variable=check1_var,onvalue='Web application development',offvalue='')
check1.pack()

check2 = tk.Checkbutton(root,text='Mobile application development',variable=check2_var,onvalue='Mobile application development',offvalue='')
check2.pack()

button = tk.Button(root,text='Click Me',command=checkbox_results)
button.pack()

label = tk.Label(root,textvariable=label_var)
label.pack()

root.mainloop()