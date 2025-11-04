# Write your MySQL query statement below

-- SELECT name 
-- FROM SalesPerson
-- WHERE name NOT IN (SELECT sp.name
-- FROM Salesperson as sp 
-- JOIN Orders as o
-- ON sp.sales_id = o.sales_id 
-- JOIN Company as c
-- ON o.com_id = c.com_id
-- WHERE c.name LIKE "RED")


SELECT sp.name
FROM Orders as o
JOIN Company as c ON c.com_id = o.com_id AND c.name  = 'RED'
RIGHT JOIN SalesPerson as sp ON o.sales_id = sp.sales_id
WHERE o.sales_id is NULL
