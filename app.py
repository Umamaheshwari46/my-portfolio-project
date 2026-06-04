import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="retail_db",
    user="dev_user",
    password="0217",
    host="localhost",
    port="5432"
)

query = "SELECT * FROM test"

df = pd.read_sql(query, conn)

st.title("Retail Database")

st.write("Rows in test table:")

st.dataframe(df)

conn.close()