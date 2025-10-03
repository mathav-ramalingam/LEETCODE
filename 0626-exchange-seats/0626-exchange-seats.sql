-- # Write your MySQL query statement below
-- SELECT s1.id, s2.student
-- FROM Seat as s1
-- INNER JOIN Seat as s2
-- ON s1.id = s2.id+1


SELECT IF(id < (SELECT MAX(id) FROM Seat), IF(id%2=0, id-1, id+1), IF(id%2=0, id-1, id)) as id, student 
FROM Seat
ORDER BY id;