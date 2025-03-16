# Write your MySQL query statement below
select emp.name , b.bonus
from Employee as emp LEFT JOIN bonus as b 
ON emp.empId = b.empId
WHERE bonus < 1000 or bonus is null