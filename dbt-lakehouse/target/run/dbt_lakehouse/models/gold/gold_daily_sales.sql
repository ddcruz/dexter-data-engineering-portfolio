
  
    
        create or replace table `workspace`.`analytics_dev_gold`.`gold_daily_sales`
      
      
    using delta
  
      
      
      
      
      
      comment 'Gold-level daily sales aggregate for BI and reporting.'
      
      as
      select
  cast(date(order_timestamp) as date) as order_date,
  count(*) as order_count,
  sum(amount) as daily_revenue,
  sum(case when is_cancelled then 1 else 0 end) as cancelled_order_count
from `workspace`.`analytics_dev_silver`.`silver_orders`
group by 1
  