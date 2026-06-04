import psycopg2

conn = psycopg2.connect(
    dbname="retail_db",
    user="dev_user",
    password="0217",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test(id SERIAL PRIMARY KEY, name TEXT);")

print("Connected successfully!")

cur.close()
conn.close()
