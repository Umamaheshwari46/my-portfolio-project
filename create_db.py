import psycopg2


#connect to default postgres database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="0217",
    host="localhost",
    port="5432"
)


conn.autocommit = True
cur = conn.cursor()


#create database
cur.execute("CREATE DATABASE retail_db;")

print("Database created successfully!")

cur.close()
conn.close()
