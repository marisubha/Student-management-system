
Student Management System (Python + MySQL + XAMPP)

This project is a simple Student Management System built using Python and MySQL.
It allows you to Add, View, Update, Delete, and Search student records easily from a command-line interface.


---

📌 Features

✔ Create database (studentdb) and table (students) automatically

✔ Add new student

✔ View all students

✔ Update specific student details

✔ Delete a student

✔ Search student by ID or Name

✔ Works with MySQL (XAMPP) using mysql.connector



---

📦 Requirements

Before running the project, install:

1️⃣ Python

Download from: https://www.python.org/

2️⃣ MySQL (XAMPP Server)

Start Apache and MySQL in XAMPP Control Panel.

3️⃣ MySQL Connector for Python

Install using:

pip install mysql-connector-python


---

⚙️ How to Run the Project

1️⃣ Start MySQL Server

Open XAMPP → Start MySQL.

2️⃣ Save the Python file

Example:

student_manager.py

3️⃣ Run the file

Use:

python student_manager.py

The program will:

Create the database studentdb

Create the table students

Show the menu options



---

🗂 Database Structure

Database Name: studentdb

Table Name: students

Column Type Description

StudentID INT (PK) Auto-increment ID
Name VARCHAR(50) Student Name
Age INT Student Age
Class VARCHAR(20) Class (ex: "10A")
Marks INT Marks out of 100



---

📘 Menu Options

1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit


---

📝 Usage

Add Student

Enter name, age, class, and marks.

View Students

Shows all students with full details.

Update Student

You can update:

Name

Age

Class

Marks


Search Student

Search by:

Student ID

Name (partial also works)


Delete Student

Removes a student by ID.


---

✔ Project Advantages

Beginner friendly

Simple and clean code

Auto database + table creation

Easy to modify for school/college projects



---

📄 License

This project is free to use for learning and academic purposes.


---

