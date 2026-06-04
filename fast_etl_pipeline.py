import pandas as pd
import json
import psycopg2
import psycopg2.extras # Critical for fast bulk loading
import time


def run_fast_pipeline():
    start_time = time.time()
    conn = psycopg2.connect(dbname="retail_db", user="dev_user", password="0217",
host="localhost")
    cur = conn.cursor()
    # 1. Load Customers (Bulk Insert)
    print("Bulk Loading 5,000 Customers...")
    df_cust = pd.read_csv('large_customers.csv')
    cust_data = [tuple(x) for x in df_cust.to_numpy()]
    psycopg2.extras.execute_values(
        cur, "INSERT INTO customers (cust_id, name, signup_date) VALUES %s", cust_data
    )
    
    
    
    # 2. Load Products (Bulk Insert)
    print("Bulk Loading 100 Products...")
    with open('large_products.json', 'r') as f:
        products = json.load(f)
    prod_data = [(p['prod_id'], p['name'], p['category'], p['price']) for p in products]
    psycopg2.extras.execute_values(
        cur, "INSERT INTO products (prod_id, name, category, price) VALUES %s", prod_data
    )



    # 3. Load 50,000 Orders (Bulk Insert)
    print("Bulk Loading 50,000 Orders (This will be very fast!)...")
    df_orders = pd.read_csv('large_orders.csv')
    order_data = [tuple(x) for x in df_orders.to_numpy()]
    psycopg2.extras.execute_values(
        cur, "INSERT INTO orders (order_id, cust_id, prod_id, quantity, order_date) VALUES %s",
order_data
    )
     
    conn.commit()
    cur.close(); conn.close()
    print(f"Pipeline completed in {round(time.time() - start_time, 2)} seconds!")



if __name__ == "__main__":
    run_fast_pipeline()
