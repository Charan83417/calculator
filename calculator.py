import tkinter as tk

def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text="Result: " + str(result))

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        result = num1 / num2
        label_result.config(text="Result: " + str(result))
    else:
        label_result.config(text="Cannot divide by zero!")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create input fields
label_num1 = tk.Label(window, text="First Number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Second Number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create buttons
button_add = tk.Button(window, text="Add", command=add)
button_add.pack()

button_subtract = tk.Button(window, text="Subtract", command=subtract)
button_subtract.pack()

button_multiply = tk.Button(window, text="Multiply", command=multiply)
button_multiply.pack()

button_divide = tk.Button(window, text="Divide", command=divide)
button_divide.pack()

# Create a label for displaying the result
label_result = tk.Label(window, text="Result: ")
label_result.pack()

# Start the main event loop
window.mainloop()
#thank you