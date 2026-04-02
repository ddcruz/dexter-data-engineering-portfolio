with source_data as (
  select *
  from {{ ref('bronze_orders') }}
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
