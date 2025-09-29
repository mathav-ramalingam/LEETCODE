# Write your MySQL query statement below
WITH Pdep as(SELECT employee_id,department_id,primary_flag FROM Employee where primary_flag = "Y")

SELECT DISTINCT e.employee_id, COALESCE(p.department_id,e.department_id) as department_id
FROM Employee as e  
LEFT JOIN Pdep as p
ON e.employee_id = p.employee_id;