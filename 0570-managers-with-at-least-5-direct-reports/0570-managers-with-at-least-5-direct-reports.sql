# Write your MySQL query statement below
SELECT e1.name from Employee as e1 
INNER JOIN Employee as e2 
ON e1.id = e2.managerId
GROUP BY e2.managerId
HAVING Count(e2.managerId) >= 5;