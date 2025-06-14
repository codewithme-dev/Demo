import tkinter as tk
from tkinter import messagebox


def show_message():
    messagebox.showinfo("Dialog", "Button Click!")


def new_window():
    root = tk.Tk()
    root.title("New Window")
    root.geometry("150x150")
    label = tk.Label(root, text = "This is new window 😀", fg = "#FF0000",font = ("Arial",50,"bold"))
    label.pack()


root = tk.Tk()
root.title("Show Message")
root.geometry("150x150")    

btn1 = tk.Button(root,text = "Show Dialog", command = show_message)
btn1.pack(pady = 20)

btn2 = tk.Button(root,text = "New Window", command = new_window)
btn2.pack(pady = 20)

root.mainloop()