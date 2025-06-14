import tkinter as tk
from tkinter import messagebox


def show_input():
    # print("You Typed: ", entry.get())
    # messagebox.showinfo("Dialog", entry.get())
    root = tk.Tk()
    root.title("New Window")
    root.geometry("150x150")
    label = tk.Label(root, text = f"{entry.get()} 😀", fg = "#FF0000",font = ("Arial",50,"bold"))
    label.pack()


root = tk.Tk()
root.title("Show Message")

entry = tk.Entry(root)
entry.pack(pady=20)

btn = tk.Button(root,text="Print Output",command=show_input)
btn.pack()

root.mainloop()