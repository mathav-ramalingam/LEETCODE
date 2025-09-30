
-- failed---
-- SELECT DISTINCT(p1.product_id), COALESCE(p2.new_price,10) as price  
-- FROM Products as p1
-- LEFT JOIN Products as p2
-- ON p1.product_id = p2.product_id AND p2.change_date <= "2019-08-16"
-- GROUP BY p1.product_id;


SELECT p1.product_id,COALESCE(
    (SELECT p2.new_price FROM Products as p2 WHERE p2.product_id = p1.product_id AND p2.change_date <= "2019-08-16" ORDER BY p2.change_date DESC LIMIT 1),10)as price
FROM (SELECT DISTINCT product_id FROM Products) as p1;


