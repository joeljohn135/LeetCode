```sql
select u.name, IF(SUM(r.distance) is NULL ,0,SUM(r.distance)) as travelled_distance from users as u LEFT JOIN rides as r on u.id=r.user_id group by user_id order by travelled_distance desc , name asc
