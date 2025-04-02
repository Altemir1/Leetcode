# Write your MySQL query statement below
select A.unique_id, B.name 
from EmployeeUNI A
right join Employees B
on A.id = B.id
