CREATE TABLE movies (
  movie_id TEXT PRIMARY KEY,
  title TEXT,
  year INT,
  genre TEXT,
  director TEXT
);

CREATE TABLE users (
  user_id INT PRIMARY KEY,
  name TEXT,
  email TEXT,
  country TEXT
);

CREATE TABLE ratings (
  user_id INT,
  movie_id TEXT,
  rating INT,
  timestamp DATE
);