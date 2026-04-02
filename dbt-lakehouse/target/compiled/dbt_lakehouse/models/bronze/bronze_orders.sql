select
  cast(order_id as string) as order_id,
  cast(customer_id as string) as customer_id,
  cast(order_timestamp as timestamp) as order_timestamp,
  cast(order_status as string) as order_status,
  cast(amount as double) as amount,
  cast(updated_at as timestamp) as updated_at
from `workspace`.`analytics_dev_bronze`.`raw_orders`