```sql
SELECT contest_id, ROUND((COUNT(R.user_id)/(SELECT COUNT(user_id) FROM Users)*100),2) as percentage
FROM Users as U INNER JOIN Register as R using(user_id)
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
