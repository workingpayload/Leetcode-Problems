# Write your MySQL query statement below
select stock_name,
sum(case when operation = 'Sell' then price end)-sum(case when operation = 'Buy' then price end) capital_gain_loss 
from stocks
group by stock_name