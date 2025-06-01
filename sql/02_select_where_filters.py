"""
SQL Foundations with Python – Day 2: SELECT, WHERE, AND, OR

🎯 Goal:
Learn how to filter and retrieve data from a database using SELECT statements in SQL.

---

🧠 What You'll Learn:
1. How to select specific columns using SELECT
2. How to filter rows using WHERE
3. How to combine conditions using AND, OR, and NOT
4. How to write readable queries using indentation

---

🛠 SQL Concepts Explained:

1. SELECT – retrieve specific columns or all (*) from a table
   Example: SELECT * FROM users

2. WHERE – filters results based on one or more conditions
   Example: SELECT * FROM users WHERE age > 25

3. AND – combines conditions, all must be true
   Example: SELECT * FROM users WHERE age > 25 AND is_active = 1

4. OR – combines conditions, at least one must be true
   Example: SELECT * FROM users WHERE is_admin = 1 OR is_verified = 1

5. NOT – inverts a condition
   Example: SELECT * FROM users WHERE NOT is_active

---
"""

from db_conn import conn, cursor

import pandas as pd


def get_data(label: str):
    """Fetch and display query results as a pandas DataFrame."""
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)

    print(f"\n🔎 {label}")
    print(df)


# 1. Select all records
cursor.execute("SELECT * FROM users")
get_data("All users")


# 2. AND condition
cursor.execute("SELECT username, email FROM users WHERE is_active = 1 AND is_verified = 1")
get_data("Users who are active AND verified")


# 3. NOT condition
cursor.execute("SELECT username, email FROM users WHERE NOT is_admin = 1")
get_data("Users who are NOT admins")


# 4. OR condition
cursor.execute("SELECT username, email FROM users WHERE username = 'Ajay' OR is_admin = 1")
get_data("Users where username is 'Ajay' OR is_admin is True")


# 5. NOT on boolean field
cursor.execute("SELECT username, email FROM users WHERE NOT is_verified")
get_data("Users who are NOT verified")


# 6. Filtering with SELECT specific columns
cursor.execute("SELECT username, age, dob FROM users WHERE age > 25")
get_data("Usernames, age, and DOB where age > 25")


# Close connection
conn.close()
