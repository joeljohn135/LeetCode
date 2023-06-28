```sql
select u.name, SUM(t.amount) as balance from users as u LEFT JOIN transactions as t on u.account=t.account group by u.account having balance>10000
