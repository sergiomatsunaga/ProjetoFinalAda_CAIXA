import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="movieflix",
    user="movieflix",
    password="movieflix"
)

cur = conn.cursor()

# MOVIES
df_movies = pd.read_csv('movies.csv')
for _, row in df_movies.iterrows():
    cur.execute("""
        INSERT INTO movies (movie_id, title, year, genre, director)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (movie_id) DO NOTHING
    """, tuple(row))

# USERS
df_users = pd.read_csv('users.csv')
for _, row in df_users.iterrows():
    cur.execute("""
        INSERT INTO users (user_id, name, email, country)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING
    """, tuple(row))

# RATINGS
df_ratings = pd.read_csv('ratings.csv')
for _, row in df_ratings.iterrows():
    cur.execute("""
        INSERT INTO ratings (user_id, movie_id, rating, timestamp)
        VALUES (%s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("✅ Dados carregados no PostgreSQL")