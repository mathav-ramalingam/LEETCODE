# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee as e
INNER JOIN Department as d
ON e.departmentId = d.id
WHERE e.salary = (SELECT MAX(Salary) FROM Employee WHERE departmentId = d.id)

