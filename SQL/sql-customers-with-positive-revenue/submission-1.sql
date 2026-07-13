-- Write your query below
Select distinct(customer_id)
FROM customers
WHERE revenue>0 AND year=2020;
