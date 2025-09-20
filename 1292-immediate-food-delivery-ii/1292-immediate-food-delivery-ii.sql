# Write your MySQL query statement below
WITH first_order as (SELECT customer_id, MIN(order_date) as order_date FROM Delivery GROUP BY customer_id)

SELECT ROUND(AVG(d.order_date = d.customer_pref_delivery_date)*100, 2) as immediate_percentage
FROM Delivery as d
INNER JOIN first_order as f
ON d.customer_id = f.customer_id AND d.order_date = f.order_date ;