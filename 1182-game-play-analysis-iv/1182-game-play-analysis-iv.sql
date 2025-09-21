# Write your MySQL query statement below
WITH first_login as (SELECT player_id, MIN(event_date) as event_date FROM Activity GROUP BY player_id)

SELECT ROUND(COUNT(DISTINCT a.player_id ) / COUNT(f.player_id),2) AS fraction
FROM first_login as f 
LEFT JOIN Activity as a 
ON f.player_id = a.player_id AND a.event_date = DATE_ADD(f.event_date, INTERVAL 1 DAY) ;