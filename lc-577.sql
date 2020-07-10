# Write your MySQL query statement below
select name, bonus
from Employee left join Bonus using(empId)
where empId not in (select empId from Bonus where bonus >= 1000);