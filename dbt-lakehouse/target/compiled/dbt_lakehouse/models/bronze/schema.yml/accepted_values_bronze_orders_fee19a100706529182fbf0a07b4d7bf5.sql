
    
    

with all_values as (

    select
        order_status as value_field,
        count(*) as n_records

    from `workspace`.`analytics_dev_bronze`.`bronze_orders`
    group by order_status

)

select *
from all_values
where value_field not in (
    'PLACED','SHIPPED','CANCELLED'
)


