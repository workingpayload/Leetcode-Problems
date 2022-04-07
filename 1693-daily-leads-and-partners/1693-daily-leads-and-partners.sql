# Write your MySQL query statement below
select date_id, make_name, count(distinct lead_id) unique_leads, count(distinct partner_id) unique_partners
from dailysales
group by date_id, make_name;
