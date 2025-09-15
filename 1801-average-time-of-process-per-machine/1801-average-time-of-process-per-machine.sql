# Write your MySQL query statement below
SELECT a.machine_id ,Round(
        (SELECT avg(a1.timestamp) FROM activity as a1 WHERE a1.activity_type = "end" and a.machine_id = a1.machine_id) -
        (SELECT avg(a1.timestamp) FROM activity as a1 WHERE a1.activity_type = "start" and a.machine_id = a1.machine_id)
    ,3)  AS processing_time
FROM Activity AS a
GROUP BY a.machine_id;