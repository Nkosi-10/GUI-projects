from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

root.iconbitmap("C:\\Users\\KHUMALO\\Desktop\\GUI-projects\\GUI_System\\cap.ico")


root.title("School Registering System.")
root.geometry("480x660")  

gender_options = ["Male", "Female", "Non-binary"]
Grade_options =["Bachelor's Pass", "Diploma Pass","Higher Certificate Pass"]

def show_students():
    # Connect to the database and fetch all records
    conn = sqlite3.connect('Student_Reg.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()

    # Clear the Text widget
    text_display.delete('1.0', END)

    # Display each student's data with labels
    for row in rows:
        student_data = (
            f"ID          : {row[0]}\n"
            f"Full Name   : {row[1]}\n"
            f"DOB         : {row[2]}\n"
            f"Gender      : {row[4]}\n"
            f"Nationality : {row[3]}\n"
            f"Phone No.   : {row[5]}\n"
            f"Address     : {row[6]}\n"
            f"Grade       : {row[8]}\n"
            f"{'-' * 50}\n"  
        )
        text_display.insert(END, student_data)



def save_to_database():
    # Retrieve user input
    fullName = Enter_Full_Name.get()
    d_o_b = Enter_Date_Of_Birth.get()
    Nationality = Enter_Nationality.get()
    gender = selected_gender.get().strip()
    school = Enter_Previous_School.get()
    phone = Enter_Phone_Number.get()
    address = Enter_Address.get()
    passgrade = selected_grade.get().strip()

    # Create/connect to the database
    conn = sqlite3.connect('Student_Reg.db')
    cursor = conn.cursor()

    # Ensure the table exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        date_of_birth TEXT,
        nationality TEXT,
        gender TEXT CHECK(gender IN ('Male', 'Female', 'Non-binary')),
        phone_number INTEGER,
        address TEXT,
        school TEXT,
        grade TEXT CHECK(grade IN ('Bachelor''s Pass', 'Diploma Pass', 'Higher Certificate Pass'))
    )''')

    try:
        # Insert data into the database
        cursor.execute(
            '''INSERT INTO students (full_name, date_of_birth, nationality, gender, phone_number, address, school, grade)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (fullName, d_o_b, Nationality, gender, phone, address, school, passgrade),
        )
        conn.commit()
        print("Data saved successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error saving data: {e}")
    finally:
        conn.close()

    # Update the Text widget with new student data
    show_students()




# The User Input 
Label(root, text ="Personal Information" , font=("Helvetica", 14)).grid( pady=7)

Enter_Full_Name = Entry(root, width=30)
Enter_Full_Name.grid(row=1, pady=5, padx=112, sticky="W")

Enter_Date_Of_Birth = Entry(root, width=30)
Enter_Date_Of_Birth.grid(row=2, padx=100, pady=5)

Enter_Nationality = Entry(root, width=30)
Enter_Nationality.grid(row=3,  pady=5)

selected_gender = StringVar()
gender_menu = ttk.Combobox(root, textvariable=selected_gender, state="readonly", width=27)
gender_menu['values'] = gender_options  # Initial options
gender_menu.grid(row=4,  pady=5)
# Enter_Gender = Entry(root, width=30)
# Enter_Gender.grid(row=4, column=1, pady=5)

Label(root, text ="Contact Details" , font=("Helvetica", 14)).grid( pady=7)

Enter_Phone_Number = Entry(root, width=30)
Enter_Phone_Number.grid(row=6,  pady=5)
Enter_Address = Entry(root, width=30)
Enter_Address.grid(row=7,  pady=5)

Label(root, text ="Academic Background", font=("Helvetica", 14)).grid( pady=7)

Enter_Previous_School = Entry(root, width=30)
Enter_Previous_School.grid(row=9,  pady=5)

selected_grade = StringVar()
grade_menu = ttk.Combobox(root, textvariable=selected_grade, state="readonly", width=27)
grade_menu['values'] = Grade_options 
grade_menu.grid(row=10,  pady=5)
# Enter_Grades = Entry(root, width=30)
# Enter_Grades.grid(row=10, column=1, pady=5)

# Labels

label_Full_Name = Label(root,text="Full Name:")
label_Full_Name.grid(row=1, pady=5, sticky="W")

label_Date_Of_Birth = Label(root,text="Date Of Birth:")
label_Date_Of_Birth.grid(row=2, pady=5, sticky="W")

label_Nationality = Label(root,text="Nationality:")
label_Nationality.grid(row=3, pady=5, sticky="W")

label_Gender = Label(root,text="Gender:")
label_Gender.grid(row=4, pady=5, sticky="W")

label_Phone_Number = Label(root,text="Phone Number:")
label_Phone_Number.grid(row=6, pady=5, sticky="W")

label_Address = Label(root,text="Address:")
label_Address.grid(row=7, pady=5, sticky="W")

label_Previous_School = Label(root,text="School Name:")
label_Previous_School.grid(row=9, pady=5, sticky="W")

def button_click():
    pass 

label_Grades = Label(root,text="Grades:")
label_Grades.grid(row=10, pady=5, sticky="W")


# button_add =Button(root, text="Register Student")
# button_add.grid(row=13, pady=15, sticky="W")

button_view =Button(root, text="Register Student" , command=save_to_database, font=("Helvetica", 10), bg="#4CAF50", fg="white", width=20)
button_view.grid(row=13, pady=10 , columnspan=3, padx=100)

text_display = Text(root, height=10, width=50)
text_display.grid(row=14, column=0, columnspan=3, padx=10, pady=10)
scrollbar = ttk.Scrollbar(root, command=text_display.yview)
scrollbar.grid(row=14, column=3, sticky='nsew')
text_display.config(yscrollcommand=scrollbar.set)




root.mainloop()