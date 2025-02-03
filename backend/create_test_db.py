import sqlite3

conn = sqlite3.connect('test_db.sqlite')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
''')

cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
])

conn.commit()
conn.close()
