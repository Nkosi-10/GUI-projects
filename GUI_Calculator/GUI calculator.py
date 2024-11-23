from tkinter import *




root = Tk()
root.title("Calculator.")
root.config(bg="#F0F8FF")
Enter = Entry(root, width=35, font=("Arial", 10))
Enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

root.iconbitmap("C:\\Users\\KHUMALO\\Desktop\\GUI-projects\\GUI_Calculator\\calc.ico")

# Global variable to store the first number and the operation
any_num = 0
maths = ""

def button_click(number):
    Enter.insert(END, number)

def clearbutton():
    Enter.delete(0, END)

def equal_button():
    global any_num
    second_num = Enter.get()
    try:
        second_num = float(second_num) 
        Enter.delete(0, END)
        
        if maths == "addition":
            Enter.insert(0, any_num + second_num)
        elif maths == "minus":
            Enter.insert(0, any_num - second_num)
        elif maths == "multiply":
            Enter.insert(0, any_num * second_num)
        elif maths == "devide":
            if second_num != 0:
                Enter.insert(0, any_num / second_num)
            else:
                Enter.insert(0, "Error")  
    except ValueError:
        Enter.insert(0, "Invalid Input") 

def plus_button():
    global any_num, maths
    maths = "addition"
    any_num = float(Enter.get())  
    Enter.delete(0, END)

def minus_button():
    global any_num, maths
    maths = "minus"
    any_num = float(Enter.get())  
    Enter.delete(0, END)

def multiply_button():
    global any_num, maths
    maths = "multiply"
    any_num = float(Enter.get())  
    Enter.delete(0, END)

def devide_button():
    global any_num, maths
    maths = "devide"
    any_num = float(Enter.get())  
    Enter.delete(0, END)

def toggle_sign():
    current_value = Enter.get()
    if current_value:
        if current_value.startswith("-"):
            Enter.delete(0, 1) 
        else:
            Enter.insert(0, "-")  

# Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_3 = Button(root, text="3", padx=41, pady=20, command=lambda: button_click(3),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_6 = Button(root, text="6", padx=41, pady=20, command=lambda: button_click(6),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_9 = Button(root, text="9", padx=41, pady=20, command=lambda: button_click(9),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0),bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_add = Button(root, text="+", padx=39, pady=20, command=plus_button,bg="#87CEFA", fg="black", bd=1, relief="solid")
button_minus = Button(root, text="- ", padx=39, pady=20, command=minus_button ,bg="#87CEFA", fg="black", bd=1, relief="solid")
button_equal = Button(root, text="=", padx=39, pady=50, command=equal_button ,bg="#00BFFF", fg="black", bd=2, relief="solid")
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply_button ,bg="#87CEFA", fg="black", bd=1, relief="solid")
button_devide = Button(root, text="/", padx=40, pady=20, command=devide_button ,bg="#87CEFA", fg="black", bd=1, relief="solid")
button_clear = Button(root, text="AC", padx=36, pady=20, command=clearbutton ,bg="#F0F8FF", fg="black", bd=1, relief="solid")
button_special = Button(root, text="+/-", padx=34, pady=20, command=toggle_sign ,bg="#F0F8FF", fg="black", bd=1, relief="solid")

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=6, column=1)
button_minus.grid(row=5, column=1)

button_multiply.grid(row=5, column=0)
button_devide.grid(row=6, column=0)

button_clear.grid(row=4, column=2)
button_special.grid(row=4, column=0)

button_equal.grid(row=5, column=2, rowspan=2, columnspan=5)

root.mainloop()

