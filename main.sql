SELECT c.customer_unique_id, 
       o.order_purchase_timestamp, 
       i.price
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
INNER JOIN order_items i
    ON o.order_id = i.order_id;

--total revenue from all customers
SELECT sum(i.price) as total_spend
FROM order_items i

--Total revenue from just the top 4,771 customers
select sum(total_spend) from 
(
    SELECT TOP 4771 c.customer_unique_id,  
           sum(i.price) as total_spend
    FROM customers c
    INNER JOIN orders o
        ON c.customer_id = o.customer_id
    INNER JOIN order_items i
        ON o.order_id = i.order_id
    GROUP BY customer_unique_id
    order by sum(i.price) desc
    )
    as top_customers

--Conclusion: Revenue concentration is low — the top 5% of customers account for only ~29% 
--of total revenue, indicating the business is not overly dependent on a small set of large 
--accounts. This reduces risk from customer churn or contract loss.

--for each customer, their customer_unique_id and their earliest order_purchase_timestamp as first_purchase_date
select c.customer_unique_id, min(o.order_purchase_timestamp) as first_purchase_date
from customers c inner join orders o
on c.customer_id = o.customer_id
group by customer_unique_id

--for retention checking
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





    