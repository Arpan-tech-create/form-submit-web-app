import sqlite3

# Create a connection to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'users'
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    phone TEXT
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()
