
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select is_cancelled
from `workspace`.`analytics_dev_silver`.`silver_orders`
where is_cancelled is null



  
  
      
    ) dbt_internal_test