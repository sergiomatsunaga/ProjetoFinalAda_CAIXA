-- Top filmes
SELECT m.title, COUNT(*) AS total_avaliacoes
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY m.title
ORDER BY total_avaliacoes DESC
LIMIT 5;

-- Melhor gênero
SELECT genre, AVG(r.rating) AS media
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY genre
ORDER BY media DESC;

-- País mais ativo
SELECT u.country, COUNT(*) AS total
FROM ratings r
JOIN users u ON r.user_id = u.user_id
GROUP BY u.country
ORDER BY total DESC;