import sqlite3
from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect("debates.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS debates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            response TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# AI response generator (simple version)
def generate_response(topic):
    responses = [
        f"The topic '{topic}' is a complex issue that requires deeper analysis.",
        f"'{topic}' has both pros and cons, depending on the context.",
        f"Debating '{topic}' involves understanding multiple perspectives.",
        f"One argument in favor of '{topic}' is its impact on society.",
        f"Many believe '{topic}' is essential, while others disagree."
    ]
    return random.choice(responses)

@app.route("/")
def home():
    conn = sqlite3.connect("debates.db")
    cursor = conn.cursor()
    cursor.execute("SELECT topic, response FROM debates ORDER BY id DESC")
    debates = cursor.fetchall()
    conn.close()
    return render_template("index.html", debates=debates)

@app.route("/debate", methods=["POST"])
def debate():
    topic = request.form["topic"]
    response = generate_response(topic)

    # Store debate in database
    conn = sqlite3.connect("debates.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO debates (topic, response) VALUES (?, ?)", (topic, response))
    conn.commit()
    conn.close()

    return render_template("index.html", topic=topic, response=response, debates=get_debates())

# Fetch all debates from the database
def get_debates():
    conn = sqlite3.connect("debates.db")
    cursor = conn.cursor()
    cursor.execute("SELECT topic, response FROM debates ORDER BY id DESC")
    debates = cursor.fetchall()
    conn.close()
    return debates

if __name__ == "__main__":
    app.run(debug=True)
