import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")

input_text = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack()

btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(btns_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                        command=lambda: calculate())
    elif button == "C":
        btn = tk.Button(btns_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                        command=lambda: clear())
    else:
        btn = tk.Button(btns_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                        command=lambda button=button: button_click(button))
    
    btn.grid(row=row, column=col, padx=1, pady=1)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

def clear():
    input_text.set("")

def calculate():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
root.mainloop()
