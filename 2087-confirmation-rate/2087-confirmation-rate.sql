SELECT s.user_id, IFNULL(ROUND(AVG(c.action = 'confirmed'),2),0) as confirmation_rate
FROM Signups as s
LEFT JOIN Confirmations as c
ON s.user_id = c.user_id 
GROUP BY s.user_id;