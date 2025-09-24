# Write your MySQL query statement below
SELECT user_id, COUNT(DISTINCT Follower_id) as followers_count
FROM Followers
GROUP BY user_id;