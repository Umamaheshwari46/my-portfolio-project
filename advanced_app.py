import streamlit as st
import pandas as pd
import psycopg2


st.set_page_config(page_title="Corporate Analytics", layout="wide")


@st.cache_data
def fetch_data():
    conn = psycopg2.connect(dbname="retail_db", user="dev_user", password="0217",
host="localhost")
    query = """
    SELECT
        o.order_date, c.name AS customer_name, p.category,
        p.price, o.quantity, (p.price * o.quantity) AS revenue
    FROM orders o
    JOIN customers c ON o.cust_id = c.cust_id
    JOIN products p ON o.prod_id = p.prod_id;
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


df = fetch_data()


# Sidebar Interactive Filters
st.sidebar.header("Filter Data")
selected_category = st.sidebar.multiselect("Product Category", options=df['category'].unique(),
default=df['category'].unique())


# Apply filters
filtered_df = df[df['category'].isin(selected_category)]


# Main Dashboard
st.title("📈 Enterprise Analytics Dashboard")


# Top Level Metrics (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered_df['revenue'].sum():,.2f}")
col2.metric("Total Orders", f"{len(filtered_df):,}")
col3.metric("Avg Order Value", f"${filtered_df['revenue'].mean():,.2f}")


st.markdown("---")


col_left, col_right = st.columns(2)


with col_left:
    st.subheader("Revenue Over Time")
    # Group by date for time-series line chart
    daily_revenue = filtered_df.groupby('order_date')['revenue'].sum()
    st.line_chart(daily_revenue)


with col_right:
    st.subheader("Revenue by Category")
    category_revenue = filtered_df.groupby('category')['revenue'].sum()
    st.bar_chart(category_revenue)


st.subheader("Raw Data Preview (Showing Top 100)")
st.dataframe(filtered_df.head(100))