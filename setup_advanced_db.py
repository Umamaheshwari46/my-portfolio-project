import psycopg2


conn = psycopg2.connect(dbname="retail_db", user="dev_user", password="0217", host="localhost")
cur = conn.cursor()


# Notice we added DATE fields, CATEGORY fields, and INDEXES
advanced_schema = """
DROP TABLE IF EXISTS orders, products, customers CASCADE;

CREATE TABLE customers (
cust_id INT PRIMARY KEY,
name VARCHAR(100),
signup_date DATE
);


CREATE TABLE products (
prod_id INT PRIMARY KEY,
name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10, 2)
);


CREATE TABLE orders (
order_id INT PRIMARY KEY,
cust_id INT REFERENCES customers(cust_id),
prod_id INT REFERENCES products(prod_id),
quantity INT,
order_date DATE
);



-- Creating Indexes for performance optimization (Mid-Level skill!)
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_products_category ON products(category);
"""

for query in advanced_schema.split(";"):
    if query.strip():
        if query:
           cur.execute(query)
        
conn.commit()
print("Advanced Tables and Indexes created!")
cur.close(); conn.close()
