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


cursor.execute("INSERT INTO tasks (subject, description, due_date, done) VALUES(?, ?, ?, ?)",
               ("Maths","All of 1J", "Monday", 0))



cursor.execute("UPDATE tasks SET done = ? WHERE subject =?",
               (1, "Maths")
               )

cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall() 
print(rows)
               

conn.commit()
conn.close()
print("Table created")