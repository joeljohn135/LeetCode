```sql
SELECT S.name
FROM SalesPerson S
LEFT JOIN (
    SELECT DISTINCT O.sales_id
    FROM Company C
    JOIN Orders O ON C.com_id = O.com_id
    WHERE C.name = 'RED'
) AS R ON S.sales_id = R.sales_id
WHERE R.sales_id IS NULL;
