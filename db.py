import psycopg2
import random

conn = psycopg2.connect(
    dbname="retail_db",
    user="dev_user",
    password="0217",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

names = [
    "Aarav", "Ravi", "Sita", "John", "Kiran",
    "Anil", "Rahul", "Priya", "David", "Sara",
    "Vikram", "Neha", "Aditi", "Rohan", "Meena"
]

# INSERT 100 PEOPLE
for i in range(1, 101):
    name = random.choice(names) + str(i)

    cur.execute("""
        INSERT INTO test (name)
        VALUES (%s)
    """, (name,))

conn.commit()

print("100 records inserted successfully!")

cur.close()
conn.close()