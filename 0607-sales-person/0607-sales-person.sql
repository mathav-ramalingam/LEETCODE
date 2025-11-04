# Write your MySQL query statement below

SELECT name 
FROM SalesPerson
WHERE name NOT IN (SELECT sp.name
FROM Salesperson as sp 
JOIN Orders as o
ON sp.sales_id = o.sales_id 
JOIN Company as c
ON o.com_id = c.com_id
WHERE c.name LIKE "RED")