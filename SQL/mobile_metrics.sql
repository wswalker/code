--this query creates basic daily metrics (retention/arpi/arppu/conversion) for d1/d7/d14/d28 based off of a generic app open table and payment
--this is going to be very time consuming and it's best to have each cte run regularly as a static table on a standard etl

--with clauses (also known as 'CTEs') make it easier to write code 
with dau as ( 
	select 
		id
		,date(timestamp) as dau_date --may need to use a different function for date depending on the sql language
	from app_open
	where 1=1 --personal preference to always begin a where clause with 1=1
		and timestamp >= '2018-01-01'
		and timestamp < date(getdate())
	group by 
		id
		,date(timestamp)
		)
,
install as (
	select 
		id
		,min(dau_date) as install_date --commas at the beginning of select terms is a personal preference
		,(date(getdate())-1)-min(dau_date) as days_since_install --going to be very important in the 'metrics' cte
	from dau -- in this situation I'm assuming the first app open is 'install'
	group by 
		id
		)
,
revenue as (
	select
		id
		,date(timestamp) as rev_date
		,sum(revenue) as rev
	from payment
	where 1=1
		and revenue >0 and revenue is not null --personal preference whenever working with revenue tables
	group by
		id
		,date(timestamp)
		)
,
customers as (
	select
		id
		,min(rev_date) as first_pay_date
	from revenue
	where 1=1
		and revenue > 0 and revenue is not null
	group by
		id
		)
,
metrics as(
	select
		a.install_date
		,count(distinct a.id) as installs --good to have an idea for volume
		,count(distinct d.id) as customers
		
		--retention metrics
		--may need to use a different date different function based on the sql language used
		--making sure the days_since_install is long enough for the retention time period is really important
		,count(distinct(case when b.dau_date-a.install_date = 1  and a.days_since_install >=1  then b.id else null end))/count(distinct a.id) as ret_d1
		,count(distinct(case when b.dau_date-a.install_date = 7  and a.days_since_install >=7  then b.id else null end))/count(distinct a.id) as ret_d7
		,count(distinct(case when b.dau_date-a.install_date = 14 and a.days_since_install >=14 then b.id else null end))/count(distinct a.id) as ret_d14
		,count(distinct(case when b.dau_date-a.install_date = 28 and a.days_since_install >=28 then b.id else null end))/count(distinct a.id) as ret_d28
		
		--I've removed D7/14/28 metrics from below for readability
		--arpi metrics
		,sum(case when c.rev_date-a.install_date = 1  and a.days_since_install >=1  then c.rev else 0 end)/count(distinct a.id) as arpi_d1
		,sum(c.rev)/count(distinct a.id) as arpi_total
		
		--arppu metrics
		,sum(case when c.rev_date-a.install_date = 1  and a.days_since_install >=1  then c.rev else 0 end)/count(distinct d.id) as arppu_d1
		,sum(c.rev)/count(distinct d.id) as arppu_total
		
		--customer conversion
		,count(distinct(case when d.first_pay_date-a.install_date = 1  and a.days_since_install >=1  then d.id else null end))/count(distince a.id) as conv_d1
		,count(distinct d.id)/count(distinct a.id) as conv_total
		
	from install a
		left join dau b
			on a.id = b.id
		left join revenue c
			on a.id = c.id
		left join customers d
			on a.id = d.id
	group by 
		a.install_date
)
select * from install -- I usually do a select * from the final table as a personal preference
