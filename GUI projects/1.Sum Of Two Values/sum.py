import tkinter as tk

root = tk.Tk()
root.title('Sum Of Two Values')
root.iconbitmap('icon.ico')
root.geometry('300x200')

def button_func(num1,num2):
    sum=num1+num2
    answer.set(f'Answer is {sum}')

number1 = tk.IntVar()
number2 = tk.IntVar()
answer = tk.StringVar()

entry1 = tk.Entry(root,textvariable=number1)
entry1.pack()

entry2 = tk.Entry(root,textvariable=number2)
entry2.pack()

button = tk.Button(root,text="Calculate",command=lambda:button_func(number1.get(),number2.get()))
button.pack()

label = tk.Label(root,textvariable=answer)
label.pack()

root.mainloop()