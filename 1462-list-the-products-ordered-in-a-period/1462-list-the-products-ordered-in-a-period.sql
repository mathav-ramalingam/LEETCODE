# Write your MySQL query statement below

WITH Fil_orders as (SELECT product_id, order_date, unit FROM Orders WHERE order_date >= '2020-02-01' AND order_date <= '2020-02-29')

SELECT p.product_name, SUM(o.unit) as unit
FROM Products as p
INNER JOIN Fil_orders as o
ON p.product_id = o.product_id 
GROUP BY p.product_name
Having SUM(o.unit) >= 100

-- SELECT * FROM Fil_orders