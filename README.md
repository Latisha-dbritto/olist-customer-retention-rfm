# Olist Customer Retention, Revenue Concentration and RFM Segmentation

I wanted to find out how an online marketplace can grow its revenue from the customers it already has. I looked at three questions:

1. Do customers come back after their first order?
2. Does most of the revenue come from a small group of customers?
3. Which customers are worth winning back?

## Data

Brazilian E-Commerce Public Dataset by Olist, from Kaggle (about 99,000 orders and 95,000 customers, 2016 to 2018). The raw files are large, so they are not in this repo. You can download them from Kaggle and run the SQL yourself.

One thing to watch in this dataset: `customer_id` changes with every order, so the same person can have many of them. `customer_unique_id` is the one that identifies a person. If you use `customer_id`, every order looks like a new customer. I used `customer_unique_id`.

## Process

1. **SQL Server:** joined the orders, customers and payments tables. Built monthly cohorts (customers grouped by the month of their first order) to measure retention, and worked out how much revenue the top 5% of customers bring.
2. **Python (pandas, matplotlib):** plotted the retention curve and built the RFM segments.
3. **Power BI:** two pages. Page 1 shows retention and revenue concentration. Page 2 shows the customer segments.

**How the RFM segments work**

- **Recency:** days since the customer's last order, counted from the latest date in the data. Scored 1 to 5 using quintiles (5 = most recent).
- **Monetary:** total spend, also scored 1 to 5 using quintiles.
- **Frequency:** about 97% of customers bought only once, so splitting frequency into five groups would not mean anything. I used a simple split instead: repeat customer or one-time buyer. Repeat customers get their own segment.
- The other segments are Recent Big Spender, Lapsed Big Spender, Recent Low Spender, Lapsed Low Spender, and Other (the middle groups that do not clearly fit any of those).

## Findings

- **Revenue is not concentrated in a few customers.** The top 5% of customers bring 29.25% of revenue.
- **Almost nobody comes back.** About 97% of customers bought only once, and retention in the months after the first order is very low. This is common for marketplaces where people buy one-off items, but it means growth depends on bringing in new customers.
- **Big spenders matter most.** Together they are about 30% of customers and about 58% of revenue.
- **Lapsed big spenders are worth winning back.** They are about 15% of customers and about 29% of revenue. One lapsed big spender is worth about R$280, which is close to a recent big spender (about R$269), and about 7 times a low spender (about R$41).

**What I would suggest:** try a win-back offer on a small group of lapsed big spenders, and compare them with a similar group that gets nothing, before rolling it out to everyone.

## Limits

- Almost everyone bought only once, so "lapsed" here only means "bought a long time ago". I cannot say these customers would respond to an offer.
- There is no cost data, so everything is revenue, not profit.
- The win-back idea is a suggestion. I have not tested it.

## Files
- [sql/](sql/): the SQL queries
- [python/](python/): `retention_analysis.py` (retention curve) and `recency.py` (RFM segments)
- [outputs/](outputs/): the small result tables
- [dashboard/](dashboard/): the Power BI file and screenshots

