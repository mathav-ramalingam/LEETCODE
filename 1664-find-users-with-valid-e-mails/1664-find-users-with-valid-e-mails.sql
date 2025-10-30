# Write your MySQL query statement below
SELECT user_id, name, mail 
FROM Users
WHERE regexp_like(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$', 'c');
