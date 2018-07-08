--this query creates a lifecycle of mobile users to assess where users are being lost in the lifecycle funnel of using an app
--this is going to be very time consuming and it's best to have each cte run regularly as a static table on a standard etl

with install as (
	select
		id
		,min(date(timestamp)) as install_date
	from app_open
	group by
		id
		)
,ftue_start_end as(
	select
		id
		,max(case when step = 1 then 1 else 0 end) as ftue_start
		,max(case when step =10 then 1 else 0 end) as ftue_end
	from ftue
	group by
		id
		)
,engagement_activities as(
	select
		id
		,max(case when activity = 'menu' then 1 else 0 end) as eng_menu
		,max(case when activity = 'click' then 1 else 0 end) as eng_click
		,max(case when activity = 'use' then 1 else 0 end) as eng_use
	from engagement
	group by
		id
		)
,customer  (
	select
		id
		,1 as pay
	from payment
	where 1=1
		and revenue > 0 and revenue is not null
	group by 
		id
		)
,lifecycle as (
	select
		a.install_date
		,count(distinct a.id) as installs
		--the coalescing is mostly helpful if there is no data joining at all (leaving a 0)
		,sum(coalesce(b.ftue_start,0)) as ftue_start 
		,sum(coalesce(b.ftue_end,0)) as ftue_end
		,sum(coalesce(c.eng_menu,0)) as eng_menu
		,sum(coalesce(c.eng_click,0)) as eng_click
		,sum(coalesce(c.eng_use,0)) as eng_use
		,sum(coalesce(d.pay,0)) as pay
	from install a
		left join ftue_start_end b
			on a.id = b.id
		left join engagement_activities c
			on a.id = c.id
		left join customer d
			on a.id = d.id
	group by 
		a.install_date
		)
select * from lifecycle

