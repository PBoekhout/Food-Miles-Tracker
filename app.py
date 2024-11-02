# app.py
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to open a connection to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    foods = conn.execute('SELECT * FROM foods').fetchall()
    conn.close()
    return render_template('index.html', foods=foods)

@app.route('/result', methods=['POST'])
def result():
    food_id = request.form['food']
    conn = get_db_connection()
    food = conn.execute('SELECT * FROM foods WHERE id = ?', (food_id,)).fetchone()
    conn.close()
    return render_template('result.html', food=food)

if __name__ == '__main__':
    app.run(port=5001)
#hi