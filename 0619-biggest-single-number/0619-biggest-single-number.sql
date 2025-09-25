# Write your MySQL query statement below
WITH res AS (SELECT num as num FROM MyNumbers GROUP BY num HAVING COUNT(num) = 1)


SELECT (CASE WHEN COUNT(*)>0 THEN MAX(num) ELSE NULL END) AS num
FROM res