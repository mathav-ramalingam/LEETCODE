# Write your MySQL query statement below

SELECT DISTINCT(t1.num) AS ConsecutiveNums 
FROM Logs as t1, Logs as t2 , Logs as t3
WHERE t1.id = t2.id+1 AND t2.id = t3.id+1 AND t1.num = t2.num AND t2.num = t3.num;
