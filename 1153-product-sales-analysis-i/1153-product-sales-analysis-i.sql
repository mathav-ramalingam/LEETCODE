select p.product_name , s.year, s.price 
from Sales s
join Product P
on s.product_id = p.product_id
