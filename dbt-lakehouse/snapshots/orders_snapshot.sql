{% snapshot orders_snapshot %}

{{
  config(
    target_schema='snapshots',
    unique_key='order_id',
    strategy='timestamp',
    updated_at='updated_at'
  )
}}

select *
from {{ ref('silver_orders') }}

{% endsnapshot %}
