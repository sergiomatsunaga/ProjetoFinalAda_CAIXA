from flask import Flask, request, jsonify

app = Flask(__name__)

movies = []

@app.route('/')
def home():
    return "MovieFlix API rodando!"

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    movies.append(data)
    return jsonify(data)

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies)

app.run(host='0.0.0.0', port=5000)
