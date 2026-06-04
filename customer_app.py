import streamlit as st
import psycopg2

# DB connection
def get_connection():
    return psycopg2.connect(
        dbname="retail_db",
        user="dev_user",
        password="0217",
        host="localhost",
        port="5432"
    )

st.title("Retail Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Customer", "View Customers"]
)

# ---------------------------
# ADD CUSTOMER FORM
# ---------------------------
if menu == "Add Customer":
    st.subheader("Insert New Customer")

    cust_id = st.number_input("Customer ID")
    name = st.text_input("Customer Name")
    signup_date = st.date_input("Signup Date")

    if st.button("Insert Customer"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO customers (cust_id, name, signup_date)
            VALUES (%s, %s, %s)
        """, (cust_id, name, signup_date))

        conn.commit()
        conn.close()

        st.success("Customer added successfully!")

# ---------------------------
# VIEW CUSTOMERS
# ---------------------------
if menu == "View Customers":
    conn = get_connection()

    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    data = cur.fetchall()

    st.write(data)

    conn.close()