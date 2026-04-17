CREATE TABLE movies (
    id INT,
    title TEXT,
    genre TEXT,
    year INT
);

CREATE TABLE users (
    id INT,
    name TEXT,
    country TEXT,
    age INT
);

CREATE TABLE ratings (
    id INT,
    user_id INT,
    movie_id INT,
    rating INT
);