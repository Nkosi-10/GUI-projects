from tkinter import *
import sqlite3 


root = Tk()


# we firstly create a database
con = sqlite3.connect("address_TA.db")
#curser creatr
c = con.cursor()

#when we create a database we use a curser

# c.execute("""CREATE TABLE addresses (
#     first_Name text,
#     surname text,
#     Age integer, 
#     Email_Address text not null
    
#     )""")

def submit():
    con = sqlite3.connect("address_TA.db")
#curser creatr
    c = con.cursor()

    
    
    
    c.execute("INSERT INTO addresses VALUES(:name, :Surname, :Age, :mail)",
              {
                  "name":name.get(),
                  "Surname":Surname.get(),
                  "Age":Age.get(),
                  "mail":mail.get(),
              })
    
    
    name.delete(0, END)
    Surname.delete(0, END)
    Age.delete(0, END)
    mail.delete(0, END)
    
    #close the connection
    con.close()
    con.commit()

def query():
    con = sqlite3.connect("address_TA.db")
#curser creatr
    c = con.cursor()
    # return

    #close the connection
    con.close()
    con.commit()
    

name =Entry(root, width=30)
name.grid(row=0, column=1, pady= 5)

Surname =Entry(root, width=30)
Surname.grid(row=1, column=1, pady=5)

Age =Entry(root, width=30)
Age.grid(row=2, column=1, pady=5)

mail =Entry(root, width=30)
mail.grid(row=3, column=1, pady=5)

name_label = Label(root, text= "Name:")
name_label.grid(row=0, column=0, pady=5)

suname_label = Label(root, text= "Surname:")
suname_label.grid(row=1, column=0, pady=5)

age_label = Label(root, text= "Age:")
age_label.grid(row=2, column=0, pady=5)

mail_label = Label(root, text= "Email:")
mail_label.grid(row=3, column=0, pady=5)

  
button_first = Button(root, width=20, text="Add Data", command=submit)
button_first.grid(row=4, column=1, pady=10)

button_second = Button(root, width=20, text="Show Data", command=query)
button_second.grid(row=5, column=1, pady=5)

#commit all the changes 
con.commit()
#close the connection
con.close()


root.mainloop()