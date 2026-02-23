import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.execute("DELETE FROM interns")
intern_data = [
    ("Hamsa", "Data Science", 15000),
    ("Bindhu", "Web Dev", 12000),
    ("Chaitra", "Data Science", 16000),
    ("Diana", "Web Dev", 13000),
    ("Varsha", "Data Science", 14000)
]
cursor.executemany("INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)", intern_data)
conn.commit()
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()


import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
print("Filter: Data Science interns with stipend > 5000")
cursor.execute("SELECT name, stipend FROM interns WHERE track='Data Science' AND stipend > 5000")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\nAggregate: Average stipend per track")
cursor.execute("SELECT track, AVG(stipend) FROM interns GROUP BY track")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("\nCount: Interns per track")
cursor.execute("SELECT track, COUNT(*) FROM interns GROUP BY track")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()



import sqlite3
import pandas as pd
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS mentors (mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,track TEXT)""")
cursor.execute("DELETE FROM mentors")
mentor_data = [
    ("Dr. Rao", "Data Science"),
    ("Ms. Sharma", "Web Dev")
]
cursor.executemany("INSERT INTO mentors (mentor_name, track) VALUES (?, ?)", mentor_data)
conn.commit()
query = """
SELECT interns.name AS intern_name, interns.track, mentors.mentor_name
FROM interns
INNER JOIN mentors ON interns.track = mentors.track
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()