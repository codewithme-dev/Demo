from tkinter import *

index = 0
text = ""

def slider():
    global index, text

    if index >= len(txt):
        index = 0
        text = ""
        label.config(text=text)
    text += txt[index]
    label.config(text=text)
    index += 1
    label.after(100, slider)  # Corrected from Label.after to label.after

root = Tk()
root.title("Sliding Text Animation")
root.geometry("1000x300")  # Optional: Set window size

txt = "Smart Solutions, Real Results"

label = Label(root, text="", font=("Arial", 30, "bold"), fg="red")
label.pack(pady=100)

slider()

root.mainloop()