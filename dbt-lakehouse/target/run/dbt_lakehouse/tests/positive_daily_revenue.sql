
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  select *
from `workspace`.`analytics_dev_gold`.`gold_daily_sales`
where daily_revenue < 0
  
  
      
    ) dbt_internal_test