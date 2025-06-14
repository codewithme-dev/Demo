import tkinter as tk


def say_hello():
    print("Hello from menu!")


root = tk.Tk()
root.title("Menu Example")


menu = tk.Menu(root)
root.config(menu=menu)


file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


root.mainloop()