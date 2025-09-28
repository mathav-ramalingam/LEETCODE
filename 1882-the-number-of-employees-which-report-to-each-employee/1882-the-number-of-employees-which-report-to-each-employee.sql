WITH emp AS (SELECT reports_to, COUNT(*) as reports_count, ROUND(AVG(age),0) as average_age
FROM Employees
WHERE reports_to is NOT NULL
GROUP BY reports_to)

SELECT e.employee_id, e.name, c.reports_count, c.average_age
FROM emp as c
INNER JOIN employees as e
ON c.reports_to = e.employee_id
ORDER BY e.employee_id;