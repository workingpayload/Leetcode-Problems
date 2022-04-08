# Write your MySQL query statement below
with cte AS
( SELECT player_id,event_date,ROW_NUMBER() OVER(PARTITION BY PLAYER_ID ORDER BY EVENT_DATE) roww from Activity )
select player_id,event_date as first_login from cte where roww=1;