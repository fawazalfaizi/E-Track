import sqlite3

with open("schema.sql") as f:
    schema = f.read()

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.executescript(schema)
conn.commit()
conn.close()


