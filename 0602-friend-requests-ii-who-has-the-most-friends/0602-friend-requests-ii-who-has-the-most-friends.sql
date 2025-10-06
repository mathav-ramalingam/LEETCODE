# Write your MySQL query statement below

WITH User AS (SELECT requester_id FROM RequestAccepted
                UNION ALL
              SELECT accepter_id FROM RequestAccepted)


SELECT requester_id as id, COUNT(*) as num
FROM User
GROUP BY id
ORDER BY num DESC
LIMIT 1;




