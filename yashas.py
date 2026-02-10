import mysql.connector

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # replace with your MySQL username
    password="root",  # replace with your MySQL password
    database="yashas" # make sure this database exists
)
cursor = conn.cursor()

# Step 2: Create table (run once)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
)
""")

# Step 3: Functions for CRUD
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    conn.commit()
    print("Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_student(student_id, new_grade):
    cursor.execute("UPDATE students SET grade=%s WHERE id=%s", (new_grade, student_id))
    conn.commit()
    print("Student updated!")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted!")

# Step 4: Menu-driven program
while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Grade")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        add_student(name, age, grade)
    elif choice == "2":
        view_students()
    elif choice == "3":
        student_id = int(input("Enter student ID: "))
        new_grade = input("Enter new grade: ")
        update_student(student_id, new_grade)
    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        delete_student(student_id)
    elif choice == "5":
        break
    else:
        print("Invalid choice, try again.")

# Close connection
cursor.close()
conn.close()