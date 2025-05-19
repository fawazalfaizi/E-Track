from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # Total minutes per user
    cur.execute("""
        SELECT users.name, SUM(activities.duration)
        FROM activities
        JOIN users ON users.id = activities.user_id
        GROUP BY users.name
    """)
    user_data = cur.fetchall()

    # Breakdown of activity types (e.g., learning vs collaboration)
    cur.execute("""
        SELECT type, SUM(duration)
        FROM activities
        GROUP BY type
    """)
    type_data = cur.fetchall()

    conn.close()

    return render_template("index.html", user_data=user_data, type_data=type_data)

if __name__ == "__main__":
    app.run(debug=True)
