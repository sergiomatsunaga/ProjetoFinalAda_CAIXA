from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
    host="localhost",
    database="movieflix",
    user="movieflix",
    password="movieflix"
    )

@app.route("/top_movies")
def top_movies():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM top_movies;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
