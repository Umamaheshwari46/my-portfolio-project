import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta


print("Generating Large Datasets...")


# 1. Generate 5,000 Customers (CSV)
cust_ids = np.arange(1, 5001)
first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
"David", "Elizabeth"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
"Rodriguez", "Martinez"]


df_cust = pd.DataFrame({
    'cust_id': cust_ids,
    'name': [f"{np.random.choice(first_names)} {np.random.choice(last_names)}"for _ in range(5000)],
    'signup_dete': [datetime(2022, 1, 1) + timedelta(days=int(d)) for d in np.random.randint(0, 700, 5000)],
})
df_cust.to_csv('large_customers.csv', index=False)



# 2. Generate 100 Products (JSON)
categories = ["Electronics", "Home", "Clothing", "Toys", "Sports"]
Products = []
for i in range(1, 101):
    Products.append({
        "prod_id": i,
        "name": f"Product_{i}",
        "category": np.random.choice(categories),
        "price": round(np.random.uniform(10.0, 500.0), 2)
    })
with open('large_products.json', 'w') as f:
        json.dump(Products, f, indent=4)


# 3. Generate 50,000 orders (CSV)
df_orders = pd.DataFrame({
    'order_id': np.arange(100001, 150001),
    'cust_id': np.random.choice(cust_ids, 50000),
    'prod_id': np.random.randint(1, 101, 50000),
    'quantity': np.random.randint(1, 6, 50000),
    'order_date': [datetime(2023, 1, 1) +timedelta(days=int(d)) for d in np.random.randint(0, 365, 50000)]

})
df_orders.to_csv('large_orders.csv', index=False)



print("Created large_customers.csv (5k rows), large_products.json (100 rows), and large_orders.csv (50k rows)!")