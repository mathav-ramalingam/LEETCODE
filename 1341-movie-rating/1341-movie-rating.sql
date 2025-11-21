-- # Write your MySQL query statement below
(SELECT u.name as results
FROM Users as u
INNER JOIN MovieRating as r
ON u.user_id = r.user_id
GROUP BY u.user_id, u.name
HAVING COUNT(r.movie_id) = 
        (SELECT MAX(movie_count) FROM (SELECT COUNT(movie_id) as movie_count FROM MovieRating GROUP BY user_id) as counts)
ORDER BY u.name
LIMIT 1
)

UNION ALL

(SELECT m.title as results
FROM Movies as m
INNER JOIN MovieRating as r
ON m.movie_id = r.movie_id AND created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY m.movie_id , m.title
ORDER BY AVG(r.rating) DESC, m.title ASC
LIMIT 1
);

