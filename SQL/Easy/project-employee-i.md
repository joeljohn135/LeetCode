```sql
Select p.project_id,ROUND(avg(e.experience_years),2) as average_years from project as p LEFT JOIN Employee as e on e.employee_id=p.employee_id group by project_id 
