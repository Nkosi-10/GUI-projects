from tkinter import *

root = Tk()
root.title("Calculator.")


Enter = Entry(root, width=35, font=("Arial", 10))
Enter.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

def button_click(number):
        Enter.insert(END, number)
        
def clearbutton():
    Enter.delete(0, END)
    

   
def equal_button():
    if maths =="addition":
        second_num =Enter.get()
        Enter.delete(0, END)
        Enter.insert(0, any_num + second_num)
    elif maths =="minus":
        second_num =Enter.get()
        Enter.delete(0, END)
        Enter.insert(0, any_num - second_num)
    elif maths =="multiply":
        second_num =Enter.get()
        Enter.delete(0, END)
        Enter.insert(0, any_num * (second_num))
    else:
        second_num =Enter.get()
        Enter.delete(0, END)
        Enter.insert(0, any_num / second_num)
        
        
    
def plus_button():
   first_num = Enter.get()
   global any_num
   global maths
   maths = "addition"
   any_num = first_num
   Enter.delete(0, END)
    
def minus_button():
       first_num = Enter.get()
       global any_num
       global maths
       maths = "minus"
       any_num = (first_num)
       Enter.delete(0, END)
    
def multiply_button():
       first_num = Enter.get()
       global any_num
       global maths
       maths = "multiply"
       any_num = (first_num)
       Enter.delete(0, END)
       
def devide_button():
       first_num = Enter.get()
       global any_num
       global maths
       maths = "devide"
       any_num = (first_num)
       Enter.delete(0, END) 
       
def toggle_sign():
    current_value = Enter.get()
    if current_value:  # Ensure the entry is not empty
        if current_value.startswith("-"):
            Enter.delete(0, 1)  # Remove the negative sign
        else:
            Enter.insert(0, "-")  # Add the negative sign at the start

    
    
    #    west world blink scene part 2
    # return
button_1 = Button(root, text="1 ", padx=40, pady=20, command= lambda:button_click(1))
button_2 = Button(root, text="2 ", padx=40, pady=20, command= lambda:button_click(2))
button_3 = Button(root, text="3 ", padx=40, pady=20, command= lambda:button_click(3))
button_4 = Button(root, text="4 ", padx=40, pady=20, command= lambda:button_click(4))
button_5 = Button(root, text="5 ", padx=40, pady=20, command= lambda:button_click(5))
button_6 = Button(root, text="6 ", padx=40, pady=20, command= lambda:button_click(6))
button_7 = Button(root, text="7 ", padx=40, pady=20, command= lambda:button_click(7))
button_8 = Button(root, text="8 ", padx=40, pady=20, command= lambda:button_click(8))
button_9 = Button(root, text="9 ", padx=40, pady=20, command= lambda:button_click(9))
button_0 = Button(root, text="0 ", padx=40, pady=20, command= lambda:button_click(0))
button_add = Button(root, text="+ ", padx=39, pady=20, command= plus_button)
button_minus = Button(root, text="-", padx=42, pady=20, command= minus_button)
button_equal = Button(root, text="= ", padx=39, pady=52, command=equal_button)
button_multiply = Button(root, text="* ", padx=40, pady=20, command= multiply_button)
button_devide = Button(root, text=" /", padx=40, pady=20, command= devide_button)
button_clear = Button(root, text="AC", padx=36, pady=20, command=clearbutton)
button_special = Button(root, text="+/-", padx=35, pady=20, command=toggle_sign)


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
button_add.grid(row=4, column=0)
button_minus.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_devide.grid(row=6, column=0)

button_clear.grid(row=5, column=1)
button_special.grid(row=6, column=1)

button_equal.grid(row=5, column=2, rowspan=2, columnspan=5)

root.mainloop()
