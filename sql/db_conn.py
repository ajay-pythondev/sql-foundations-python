import sqlite3

# Create a global connection object
conn = sqlite3.connect("tutorial.db", check_same_thread=False)

# Create a global cursor
cursor = conn.cursor()
