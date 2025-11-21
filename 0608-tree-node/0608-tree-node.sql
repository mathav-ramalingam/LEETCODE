# Write your MySQL query statement below
WITH parent AS (SELECT p_id FROM Tree WHERE p_id IS NOT NULL)


SELECT id, CASE  
WHEN p_id IS NULL THEN "Root"
WHEN id IN (SELECT p_id FROM parent) THEN "Inner"
ELSE "Leaf"
END AS type 
FROM Tree