import tkinter as tk


my_file = tk.Tk()
my_file.title("Hello TKinter")
my_file.geometry("150x150")
label = tk.Label(my_file, text = "Hello World!")
label.pack()
label = tk.Label(my_file, text = "Welcome to my page 😀", fg = "#FF0000",font = ("Arial",50,"bold"))
label.pack()

my_file.mainloop()