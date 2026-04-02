
  
  
  create or replace view `workspace`.`analytics_dev_silver`.`silver_orders`
  (
    `order_id`,
	`customer_id`,
	`order_timestamp`,
	`order_status`,
	`amount`,
	`updated_at`,
	`is_cancelled`
  )
  comment 'Cleaned order data with normalized status and cancellation flag.'
  as (
    with source_data as (
  select *
  from `workspace`.`analytics_dev_bronze`.`bronze_orders`
)

select
  order_id,
  customer_id,
  order_timestamp,
  upper(trim(order_status)) as order_status,
  amount,
  updated_at,
  case when upper(trim(order_status)) = 'CANCELLED' then true else false end as is_cancelled
from source_data
where amount >= 0
  )
