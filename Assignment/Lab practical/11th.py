#Q11. Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

# Program: SQLite3 Database Example in Python

import sqlite3   # Importing sqlite3 module

# 1. Connect to SQLite3 Database (if not exist, it will be created)
conn = sqlite3.connect("student.db")

# 2. Create a cursor object
cursor = conn.cursor()

# 3. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# 4. Insert some data
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Jay Sompura", 22, "Python Programming"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Ankit", 21, "C++ Programming"))
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", ("Priya", 23, "Data Science"))

# 5. Commit changes (to save data)
conn.commit()

# 6. Fetch all data from the table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# 7. Print fetched data
print("Student Records:")
for row in rows:
    print(row)

# 8. Close the connection
conn.close()
