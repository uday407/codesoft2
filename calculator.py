from tkinter import *

# Create a function to handle button clicks
def btn_click(item):
    global expression
    if expression == "0":
        expression = str(item)
    else:
        expression = expression + str(item)
    input_text.set(expression)

# Create a function to clear the calculator display
def bt_clear():
    global expression
    expression = "0"
    input_text.set(expression)

# Create a function to evaluate the expression and display the result
def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# Create the main GUI window
win = Tk()
win.title("Calculator")
win.geometry("312x400")  # Increased height to accommodate more buttons
win.resizable(0, 0)

# Initialize the expression variable and input text variable for display
expression = "0"
input_text = StringVar()
input_text.set(expression)

# Create a frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="blue", highlightcolor="red", highlightthickness=2)
input_frame.pack(side=TOP)

# Create an entry widget to display the calculator input/output
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="aqua", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Create a frame for the calculator buttons
button_fr = Frame(win, width=312, height=352)
button_fr.pack()

# Define button labels and their respective commands
buttons = [
    ("C", bt_clear), ("/", lambda: btn_click("/")), ("7", lambda: btn_click(7)), ("8", lambda: btn_click(8)),
    ("9", lambda: btn_click(9)), ("*", lambda: btn_click("*")), ("4", lambda: btn_click(4)), ("5", lambda: btn_click(5)),
    ("6", lambda: btn_click(6)), ("-", lambda: btn_click("-")), ("1", lambda: btn_click(1)), ("2", lambda: btn_click(2)),
    ("3", lambda: btn_click(3)), ("+", lambda: btn_click("+")), ("0", lambda: btn_click(0)), (".", lambda: btn_click(".")),
    ("=", bt_equal)
]

# Create and place the calculator buttons using a loop
row_idx, col_idx = 1, 0
for (btn_text, btn_command) in buttons:
    Button(button_fr, text=btn_text, width=7, height=3, bd=0, bg="white", cursor="hand2", font=("Arial", 12, "bold"), command=btn_command).grid(row=row_idx, column=col_idx, padx=4, pady=4)
    col_idx += 1
    if col_idx > 3:
        col_idx = 0
        row_idx += 1

# Start the main event loop
win.mainloop()