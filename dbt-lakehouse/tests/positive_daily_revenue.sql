select *
from {{ ref('gold_daily_sales') }}
where daily_revenue < 0
