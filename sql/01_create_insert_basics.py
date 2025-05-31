"""
SQL Foundations with Python – Day 1: CREATE, INSERT, UPDATE, DELETE

🎯 Goal:
Learn how to use SQL with Python to interact with a relational database using SQLite.

---

🧠 What You'll Learn:
1. How to create a table to store data
2. How to insert new records into a table
3. How to update existing data
4. How to retrieve data using SELECT
5. How to delete specific records
6. How to remove the table (cleanup)

---

📘 SQL Concepts Explained:

1. CREATE TABLE – defines a new table and its columns
   Example: CREATE TABLE users (id INTEGER, name TEXT)

2. INSERT INTO – adds a new row to a table
   Example: INSERT INTO users (name) VALUES ('Ajay')

3. UPDATE – modifies existing data in rows
   Example: UPDATE users SET name = 'Ajay Dev' WHERE id = 1

4. SELECT – read data from the table
   Example: SELECT * FROM users

5. DELETE – removes one or more rows
   Example: DELETE FROM users WHERE id = 2

6. DROP TABLE – deletes the table completely
   Example: DROP TABLE users

---

🛠 Tools We're Using:

✔️ sqlite3
This is Python’s built-in library to interact with SQLite databases (no extra installation required).

✔️ datetime
Used to store and update timestamps (like `last_login`).

---

🔄 Understanding conn and cursor

- `conn` = connection object
  It represents the connection to your SQLite database file (or creates one if it doesn’t exist).

- `cursor` = cursor object
  Think of this as your SQL executor. It sends SQL queries to the database and receives results back.

Typical flow:
1. You connect to the database: `conn = sqlite3.connect(...)`
2. You create a cursor: `cursor = conn.cursor()`
3. You use `cursor.execute(...)` to run SQL
4. You fetch results (if needed) using `cursor.fetchall()` or `.fetchone()`
5. You save changes using `conn.commit()`
6. You close everything using `conn.close()`

---

💾 What does conn.commit() do?

- It saves all the changes (INSERT, UPDATE, DELETE) you've made to the database.
- If you don't commit, your changes will be lost when the script ends.
- Always call `conn.commit()` before closing the connection.

📕 What does conn.close() do?

- It properly shuts down the connection to the database.
- Frees up system resources.
- Prevents database file locks or memory leaks.

Think of it like writing to a file — always save and close it when you're done.
"""


import sqlite3
from datetime import datetime

conn = sqlite3.connect("tutorial.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        age INTEGER,
        dob DATE,
        password TEXT,
        email TEXT,
        is_admin BOOLEAN DEFAULT FALSE NOT NULL,
        is_active BOOLEAN DEFAULT FALSE NOT NULL,
        is_verified BOOLEAN DEFAULT FALSE NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    )"""
)

cursor.execute("""INSERT INTO users (username, age, dob, password, email, is_admin, is_active) 
                  VALUES (?, ?, ?, ?, ?, ?, ?)""", ("ajay", 29, "05-02-1996", "pass@1234", "ajay@example.com", True, True))

cursor.execute("""INSERT INTO users (username, age, dob, password, email, is_admin, is_active) 
                  VALUES (?, ?, ?, ?, ?, ?, ?)""", ("ajay", 29, "05-02-1996", "pass@1234", "ajay@example.com", True, False))

cursor.execute("""UPDATE users SET is_admin = ?, last_login= ? WHERE id = 2""", (True, datetime.now()))

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.execute("""DELETE FROM users WHERE id = 2""")

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.execute("""DROP TABLE IF EXISTS users""")

conn.commit()

conn.close()
