# Write your MySQL query statement below
SELECT u.name as name, IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users as u
LEFT JOIN Rides as r
ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, name ASC;