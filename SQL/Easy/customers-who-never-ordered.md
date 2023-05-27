```sql
Select c.name as Customers from customers as c where c.id not in (select customerId from orders)
