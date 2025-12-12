import mysql.connector

# ------------------ DATABASE CONNECTION ------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

# ------------------ CREATE DATABASE ------------------
cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
cursor.execute("USE studentdb")

# ------------------ CREATE TABLE ------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Class VARCHAR(20),
    Marks INT
)
""")

db.commit()


# ------------------ ADD STUDENT ------------------
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    clas = input("Enter Class: ")
    marks = int(input("Enter Marks: "))

    query = "INSERT INTO students (Name, Age, Class, Marks) VALUES (%s, %s, %s, %s)"
    values = (name, age, clas, marks)

    cursor.execute(query, values)
    db.commit()

    print("\n✔ Student Added Successfully!\n")


# ------------------ VIEW ALL STUDENTS ------------------
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n----- All Students -----\n")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Class: {row[3]} | Marks: {row[4]}")
    print()


# ------------------ UPDATE STUDENT ------------------
def update_student():
    student_id = input("Enter Student ID to update: ")

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Class")
    print("4. Marks")

    choice = input("Choose an option: ")

    field_map = {
        "1": "Name",
        "2": "Age",
        "3": "Class",
        "4": "Marks"
    }

    if choice in field_map:
        new_value = input(f"Enter new {field_map[choice]}: ")

        query = f"UPDATE students SET {field_map[choice]} = %s WHERE StudentID = %s"
        cursor.execute(query, (new_value, student_id))
        db.commit()

        print("\n✔ Student Updated Successfully!\n")
    else:
        print("\n❌ Invalid Option!\n")


# ------------------ DELETE STUDENT ------------------
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE StudentID = %s", (student_id,))
    db.commit()

    print("\n🗑 Student Deleted Successfully.\n")


# ------------------ SEARCH STUDENT ------------------
def search_student():
    keyword = input("Enter Student Name or ID: ")

    if keyword.isdigit():
        cursor.execute("SELECT * FROM students WHERE StudentID = %s", (keyword,))
    else:
        cursor.execute("SELECT * FROM students WHERE Name LIKE %s", ("%" + keyword + "%",))

    rows = cursor.fetchall()

    print("\n----- Search Results -----\n")
    if rows:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Class: {row[3]} | Marks: {row[4]}")
    else:
        print("No student found.")
    print()


# ------------------ MAIN MENU ------------------
def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Input. Try again.\n")


main()
