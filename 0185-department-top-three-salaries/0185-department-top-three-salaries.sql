# Write your MySQL query statement below

Select dep.name AS Department, emp.name AS Employee, emp.salary
from Department as dep
JOIN Employee as emp 
ON emp.DepartmentId=dep.Id 
WHERE (Select count(distinct Salary) From Employee 
       where DepartmentId=dep.Id and Salary>=emp.Salary) <= 3
ORDER BY Department , Salary




