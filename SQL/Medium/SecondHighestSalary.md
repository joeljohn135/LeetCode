```sql
Select MAX(salary) as secondhighestsalary from Employee where salary<(select MAX(Salary) from Employee )
