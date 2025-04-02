# Write your MySQL query statement below
select sales.year, sales.price, product.product_name
from Sales sales
inner join Product product
on sales.product_id = product.product_id
