import json, sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

with open("data.json") as f:
    users = json.load(f)
    for user in users:
        cur.execute("INSERT INTO users (name) VALUES (?)", (user['name'],))
        user_id = cur.lastrowid
        for act in user['activities']:
            cur.execute("""
                INSERT INTO activities (user_id, activity, type, duration, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, act['activity'], act['type'], act['duration'], act['timestamp']))

conn.commit()
conn.close()
