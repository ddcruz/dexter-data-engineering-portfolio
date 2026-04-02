
      
  
    
        create or replace table `workspace`.`snapshots`.`orders_snapshot`
      
      
    using delta
  
      
      
      
      
      
      
      
      as
      select *,
        md5(coalesce(cast(order_id as string ), '')
         || '|' || coalesce(cast(updated_at as string ), '')
        ) as dbt_scd_id,
        updated_at as dbt_updated_at,
        updated_at as dbt_valid_from,
        
  
  coalesce(nullif(updated_at, updated_at), null)
  as dbt_valid_to

    from (
        select *
from `workspace`.`analytics_dev_silver`.`silver_orders`
    ) sbq


  
  