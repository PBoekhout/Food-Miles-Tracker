# init_db.py
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Sample data
foods = [
    ('Bananas', 2500),
    ('Apples', 1500),
    ('Coffee', 3000),
    ('Beef', 500),
    ('Rice', 2000)
]

cur.executemany("INSERT INTO foods (name, distance) VALUES (?, ?);", foods)

connection.commit()
connection.close()
