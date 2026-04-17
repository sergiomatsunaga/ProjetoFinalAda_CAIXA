CREATE VIEW top_movies AS
SELECT m.title, AVG(r.rating) avg_rating
FROM movies m
JOIN ratings r ON m.id = r.movie_id
GROUP BY m.title
ORDER BY avg_rating DESC;