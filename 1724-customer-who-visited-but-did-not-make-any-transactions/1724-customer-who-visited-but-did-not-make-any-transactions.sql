# Write your MySQL query statement below
SELECT v.customer_id, Count(v.visit_id) as count_no_trans
FROM Visits as v 
LEFT JOIN Transactions as t
ON v.visit_id = t.visit_id
WHERE t.transaction_id is NULL
GROUP BY v.customer_id;