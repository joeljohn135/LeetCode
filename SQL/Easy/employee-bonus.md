```sql
Select e.name,b.bonus from employee as e LEFT JOIN  Bonus as b ON e.empId=b.empId where bonus<1000 or bonus is null
