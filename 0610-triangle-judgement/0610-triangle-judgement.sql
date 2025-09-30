# Write your MySQL query statement below

-- SELECT x, y ,z, CASE WHEN x+y > z AND y+z > x AND z+x > y THEN 'Yes' ELSE 'No' END as triangle
-- FROM Triangle;

-- OR


SELECT x, y ,z, IF (x+y > z AND y+z > x AND z+x > y, 'Yes','No') as triangle
FROM Triangle;


