import pandas as pd

df = pd.read_csv('SQL/rfm_base.csv', usecols=[0, 1, 2, 3])
df.columns = ['customer_unique_id', 'last_order', 'num_orders', 'total_spend']

#Recency
df['last_order'] = pd.to_datetime(df['last_order'])
base = df['last_order'].max()
df['recency_days'] = (base - df['last_order']).dt.days

df['r_score'] = pd.qcut(df["recency_days"], 5, labels= [5,4,3,2,1])
# print(df.groupby('r_score')['recency_days'].agg(['min', 'max']))

#Monetary
df['m_score'] = pd.qcut(df["total_spend"], 5, labels= [1,2,3,4,5])
# print(df.groupby('m_score')['total_spend'].agg(['min', 'max']))

#Frequency
df['is_repeat'] = df['num_orders'] >= 2
# print(df['is_repeat'].value_counts())

#Segmentation
df['r_score'] = df['r_score'].astype(int)
df['m_score'] = df['m_score'].astype(int)
df['Segment'] = "Other"
df.loc[(df['m_score'] >= 4) & (df['r_score'] >= 4), 'Segment'] = "Recent Big Spender"
df.loc[(df['m_score'] >= 4) & (df['r_score'] <= 2), 'Segment'] = "Lapsed Big Spender"
df.loc[(df['m_score'] <= 2) & (df['r_score'] >= 4), 'Segment'] = "Recent Low Spender"
df.loc[(df['m_score'] <= 2) & (df['r_score'] <= 2), 'Segment'] = "Lapsed Low Spender"
df.loc[df['is_repeat']==True, 'Segment'] = "Repeat Customer"

summary = df.groupby('Segment').agg(
    customers = ('customer_unique_id', 'count'),
    revenue = ('total_spend', 'sum'),
)
summary['revenue_pct'] =  (summary['revenue']/ summary['revenue'].sum())*100
print(summary)
summary.reset_index().to_csv('SQL/rfm_summary.csv', index=False)
