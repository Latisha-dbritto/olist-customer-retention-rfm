--Retention
select month_offset, count(distinct customer_unique_id) as customer_count from(
    select cohorts.customer_unique_id, first_purchase_date, o.order_purchase_timestamp, 
    DATEDIFF(month, first_purchase_date, order_purchase_timestamp) AS month_offset from
    (
        select c.customer_unique_id, min(o.order_purchase_timestamp) as first_purchase_date
        from customers c inner join orders o
        on c.customer_id = o.customer_id
        group by customer_unique_id) 
    as cohorts 
    inner join customers c
    on c.customer_unique_id = cohorts.customer_unique_id 
    inner join orders o
    on o.customer_id = c.customer_id) as retention
group by month_offset