# Write your MySQL query statement below
SELECT 
    visited_on,
    (SELECT SUM(c2.amount) 
        FROM Customer AS c2
        WHERE c2.visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on) as amount,
    ROUND((SELECT SUM(c2.amount)/7 
        FROM Customer AS c2
        WHERE c2.visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on),2) as average_amount
FROM Customer as c
WHERE c.visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM Customer)
GROUP BY visited_on
ORDER BY c.visited_on
