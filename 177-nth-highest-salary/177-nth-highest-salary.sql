CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select salary from (
select salary, row_number() over(order by salary desc) as rnk
from (select distinct salary from employee)intd )fnl where rnk = N
      
  );
END