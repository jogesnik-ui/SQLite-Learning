import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY,
               subject TEXT,
               description TEXT,
               due_date TEXT,
               done INTEGER)
""")

conn.commit()
conn.close()
print("Table created")