# Write your MySQL query statement belo
SELECT DISTINCT p.product_id, p.product_name
FROM Product as p
LEFT JOIN Sales as s
ON p.product_id = s.product_id
WHERE s.sale_date >= '2019-01-01' AND s.sale_date <= '2019-03-31' 
AND p.product_id not in (SELECT product_id from sales WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31')

