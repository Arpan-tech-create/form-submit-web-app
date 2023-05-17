from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to create a connection and cursor
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn, conn.cursor()

# Create the initial database if it doesn't exist
def create_database():
    conn, cursor = get_db_connection()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['nm']
        email = request.form['mail']
        phone = request.form['num']

        conn, cursor = get_db_connection()
        cursor.execute('INSERT INTO submissions (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        conn.commit()
        conn.close()

        return render_template('success.html')

    return render_template('index.html')

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5005)
