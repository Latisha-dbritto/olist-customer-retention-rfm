import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SQL/Retention.csv', header=None)
df.columns = ['month_offset', 'customer_count']

base = df.loc[df['month_offset'] == 0, 'customer_count'].values[0]

df['retention_percent'] = (df['customer_count'] / base) * 100
df['retention_percent'] = df['retention_percent'].round(2)

plt.plot(df['month_offset'], df['retention_percent'])
plt.title('Customer Retention Curve')
plt.xlabel('Months Since First Purchase')
plt.ylabel('Retention %')
plt.show()
df.to_csv('SQL/retention_clean.csv', index=False)