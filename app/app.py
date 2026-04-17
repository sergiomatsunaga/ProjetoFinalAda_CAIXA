from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "MovieFlix API rodando"}

@app.route('/movies')
def movies():
    conn = psycopg2.connect("dbname=movieflix user=user password=password host=db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies LIMIT 10")
    rows = cur.fetchall()
    return jsonify(rows)

app.run(host='0.0.0.0', port=5000)