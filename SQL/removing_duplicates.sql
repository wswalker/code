--this query removes dups from a generic install table

with dup_install as (
	select
		id --in this table there are multiple records for the same d
		,timestamp
		,source
		,row_number()over(partition by id order by timestamp asc) as rown
		)
,no_dup_install as (
	select
		id
		,timstamp
		,source
	from dup_install
	where 1=1
		and rown =1 --this will take the first install for ever id
		)
select * from no_dup_install
