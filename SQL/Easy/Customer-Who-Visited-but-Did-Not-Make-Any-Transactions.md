```sql
select v.customer_id , count(v.visit_id) as count_no_trans from Visits as v LEFT JOIN transactions as t on v.visit_id=t.visit_id where t.visit_id is NULL group by v.customer_id order by count_no_trans
