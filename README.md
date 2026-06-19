

# my-portfolio-project
**My Data Analytics Project**
**Retail Management System & Enterprise Analytics Dashboard**


**Project Overview**

This project demonstrates the complete lifecycle of a retail data analyticssolution using Python, PostgreSQL, Pandas, Numpy, and Streamlit.

The project consists of four major stages:

1. Large-scale dataset generation
2. Database schema creation and optimization
3. High-performance ETL(Extract, Transform, Load)pipeline
4. Interactive analytics dashboard

The goal of this project is to simulate a real-world retail environment by generating thousands of customer records, product records,and order transactions, storing them in PostgreSQL, and visualizing business insights through an interactive Streamlit dashboard.


**Techologies Used**

Python
PostgreSQL
Streamlit
Pandas
Psycopg2
JSON
CSV

**Project Architecture**

Dataset Generation
↓
CSV / JSON Files
↓
ETL Pipeline
↓
PostgreSQL Database
↓
SQL Analytics Queries
↓
Streamlit Dashboard

**Project Components**
1.Data Generation Module

Objective

Generate realistic retail datasets for analytics and reporting.

Generated Files

Customers Dataset

File:

    large_customers.csv

Records:

    5,000 Customers

Fields:

    cust_id
    name
    signup_date

Products Dataset

File:

    large_products.json

Records:

    100 Products

Fields:

    prod_id
    name
    category
    price

Orders Dataset

File:

    large_orders.csv

Records:

    50,000 Orders

Fields:
    order_id
    cust_id
    prod_id
    quantity
    order_date

**Key Concepts Demonstrated**

    Random data generation
    CSV file creation
    JSON file creation
    Data engineering fundamentals


**2. Database Schema Design **

    Database:

    retail_db

    Tables:

    Customers

Stores customer information.


**Column	   Type**
  cust_id	   INT
  name	           VARCHAR
  signup_date	   DATE

**Products**

 Stores product catalog information.

**Column	       Type**

    prod_id	       INT
    name	       VARCHAR
    category	       VARCHAR
    price	       DECIMAL

**Orders**

 Stores transactional order information.

 ** Column	     Type**

    order_id	 INT
    cust_id	     INT
    prod_id	     INT
    quantity	 INT
    order_date	 DATE

Relationships

  orders.cust_id → customers.cust_id
  orders.prod_id → products.prod_id

Database Optimization

 Indexes created:
    idx_orders_date
    idx_products_category

purpose:

      Faster filtering
      Faster analytical queries
      Improved dashboard performance

**3.ETL Pipeline**
  Objective
    
    Load large datasets into PostgreSQL efficiently.

  Process

    step 1:
    Load customer CSV data

    step 2:
    Load product JSON data

    step 3:
    Load order CSV data
  
  Performance Optimization
    
    Used:

    psycopg2.extras.execute_values()

    Benefits:
        Bulk inserts
        Reduced database round trips
        Significantly faster loading than row-by-row inserts
    
    Dataset Size
        
        5,000 Customers
        100 Products
        50,000 Orders
     
     Total Records Loaded:
     55,100+


**4. Enterprise Analytics Dashboard Technology**

   Streamlit

   Features

   KPI Cards

    Total Revenue
    Total Orders
    Average Order Value


 **Interactive Filters**

   Filter by:

        Product Category

    Revenue Trend Analysis

     Line chart showing revenue over time.

    Category Performance Analysis

     Bar chart displaying revenue by product category.

    Data Exploration
     Interactive table displaying transaction-level records.


**SQL Analytics Query**

The dashboard uses SQL joins to combine information from multiple tables,

Table Joined:
    
    customers
    products
    orders

Calculate Metric:

Revenue = Price × Quantity

This demonstrates practical SQL skills and relational database design


Skills Demonstrated

**Python**

    Functions
    File handling
    Data processing
    Automation

**PostgreSQL**

    Database creation
    Table design
    Foreign keys
    Indexes
    SQL joins

**Data Engineering**

    ETL pipeline development
    Bulk data loading
    CSV and JSON processing 

**Data Analytics**
    KPI calculation
    Aggregation
    Trend analysis

**Streamlit**
    Interactive dashboard creation
    User filters
    Data visualization   


**Project Results**

Successfully created:

    5,000 customer records
    100 product records
    50,000 order records
    Optimized PostgreSQL database
    Automated ETL pipeline
    Interactive business intelligence dashboard

 This project simulates a real-world retail analytics environment and demonstrates skills commonly required for Data Analyst, Business Analyst, Data Engineer, and Python Developer roles.

**Future Enhancements**

   Customer segmentation analysis
   Product recommendation engine
   Forecasting sales using machine learning
   Real-time dashboard updates
   User authentication system
   Deployment on cloud platforms


Author

Puma Maheshwari

Retail Analytics & Data Engineering Portfolio Project

