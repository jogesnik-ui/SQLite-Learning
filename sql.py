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

def add_task(cursor, subject, description, due_date, done):
    cursor.execute(
        "INSERT INTO tasks (subject, description, due_date, done) VALUES(?, ?, ?, ?)",
            (subject, description, due_date, 0))
    
def complete_task(cursor, conn, subject):
    cursor.execute("UPDATE tasks SET done = ? WHERE subject =?",
                   ( 1, subject))
    conn.commit()


def get_tasks(conn, cursor, subject):
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    print (rows)
              
               
#Add Tasks  
add_task(cursor, "Maths","All of 1J", "Monday", 0)
add_task(cursor, "English", "Essay draft", "Tuesday", 0)
add_task(cursor, "Science", "Lab report", "Wednesday", 0)

cursor.execute("DELETE FROM tasks WHERE subject=?",
               ("Maths",)
               )



#Mark English done
complete_task(cursor, conn, "English")

#Get all tasks
get_tasks(conn, cursor, "subject")


conn.commit()
 


conn.close()
print("Table created!")


