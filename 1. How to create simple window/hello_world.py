import tkinter as tk

# create a window
root = tk.Tk()

width, height = 400,400

#How to open center in the screen
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}') #widthxheight+left+top

root.title("Hello World")
root.iconbitmap('icon.ico')

root.resizable(False,True)#cannot resize in width

# run the window
root.mainloop()