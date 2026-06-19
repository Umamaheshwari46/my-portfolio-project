

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



# 🚀 Retail Data Engineering & Analytics Portfolio Project

## 📌 About the Project

This project is a **data engineering and analytics system** built using Python and PostgreSQL.
It demonstrates how to generate, store, and process large-scale retail datasets for reporting and analysis.

The project is designed for **portfolio building and job readiness (Data Entry / Junior Developer / Data Analyst roles).**

---

## 🛠️ Tech Stack

* Python 3
* PostgreSQL
* Pandas
* Streamlit
* psycopg2
* Ubuntu (Linux environment)

---

## 📌 Step 1: Install Required Tools

### Update system packages

```bash
sudo apt update
```

### Install Python and tools

```bash
sudo apt install python3 python3-pip python3-venv -y
```

### Install PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib -y
```

### Install PostgreSQL development library

```bash
sudo apt install libpq-dev -y
```

---

## 📌 Step 2: Configure PostgreSQL Database

### Login to PostgreSQL

```bash
sudo -i -u postgres
psql
```

### Create database and user

```sql
CREATE DATABASE retail_db;

CREATE USER junior_dev WITH PASSWORD 'securepass';

GRANT ALL PRIVILEGES ON DATABASE retail_db TO junior_dev;

ALTER DATABASE retail_db OWNER TO junior_dev;
```

### Exit

```bash
\q
exit
```

---

## 📌 Step 3: Setup Python Environment

### Create project folder

```bash
mkdir my_portfolio_project
cd my_portfolio_project
```

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate environment

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install pandas psycopg2 streamlit
```

---

## 📌 Step 4: Run the Project

### Run database script

```bash
python create_db.py
```

### OR launch dashboard

```bash
streamlit run app.py
```

---

## 📊 Project Modules

### 1️⃣ Data Generation Module

Generates realistic retail datasets for analytics.

#### 📁 Customers Dataset

* File: `large_customers.csv`
* Records: 5,000 customers

Fields:

* cust_id
* name
* signup_date

---

#### 📁 Products Dataset

* File: `large_products.json`
* Records: 100 products

Fields:

* prod_id
* name
* category
* price

---

#### 📁 Orders Dataset

* File: `large_orders.csv`
* Records: 50,000 orders

Fields:

* order_id
* cust_id
* prod_id
* quantity
* order_date

---

## 🎯 Project Goals

* Practice real-world data handling
* Learn PostgreSQL integration with Python
* Build portfolio-ready project
* Improve backend + analytics skills

---
## 📚 Key Concepts Demonstrated

* Random data generation
* CSV file creation
* JSON file creation
* Data engineering fundamentals

---

## 🗄️ Database Schema Design

### Database

`retail_db`

### Customers Table

Stores customer information.

| Column      | Type    |
| ----------- | ------- |
| cust_id     | INT     |
| name        | VARCHAR |
| signup_date | DATE    |

### Products Table

Stores product catalog information.

| Column   | Type    |
| -------- | ------- |
| prod_id  | INT     |
| name     | VARCHAR |
| category | VARCHAR |
| price    | DECIMAL |

### Orders Table

Stores transactional order information.

| Column     | Type |
| ---------- | ---- |
| order_id   | INT  |
| cust_id    | INT  |
| prod_id    | INT  |
| quantity   | INT  |
| order_date | DATE |

### Relationships

* orders.cust_id → customers.cust_id
* orders.prod_id → products.prod_id

### Database Optimization

Indexes created:

* idx_orders_date
* idx_products_category

#### Purpose

* Faster filtering
* Faster analytical queries
* Improved dashboard performance

---

## 🔄 ETL Pipeline

### Objective

Load large datasets into PostgreSQL efficiently.

### Process

#### Step 1

Load customer CSV data

#### Step 2

Load product JSON data

#### Step 3

Load order CSV data

### Performance Optimization

Used:

```python
psycopg2.extras.execute_values()
```

Benefits:

* Bulk inserts
* Reduced database round trips
* Faster loading than row-by-row inserts

### Dataset Size

| Dataset   | Records |
| --------- | ------- |
| Customers | 5,000   |
| Products  | 100     |
| Orders    | 50,000  |

### Total Records Loaded

**55,100+ Records**

---

## 📊 Enterprise Analytics Dashboard

### Technology

**Streamlit**

### Features

#### KPI Cards

* Total Revenue
* Total Orders
* Average Order Value

#### Interactive Filters

Filter by:

* Product Category

#### Revenue Trend Analysis

Line chart showing revenue over time.

#### Category Performance Analysis

Bar chart displaying revenue by product category.

#### Data Exploration

Interactive table displaying transaction-level records.

---

## 🧾 SQL Analytics Query

The dashboard uses SQL joins to combine data from multiple tables.

### Tables Joined

* customers
* products
* orders

### Calculated Metric

```text
Revenue = Price × Quantity
```

This demonstrates practical SQL skills and relational database design.

---

## 💡 Skills Demonstrated

### Python

* Functions
* File handling
* Data processing
* Automation

### PostgreSQL

* Database creation
* Table design
* Foreign keys
* Indexes
* SQL joins

### Data Engineering

* ETL pipeline development
* Bulk data loading
* CSV processing
* JSON processing

### Data Analytics

* KPI calculation
* Aggregation
* Trend analysis

### Streamlit

* Interactive dashboard creation
* User filters
* Data visualization

---

## 🎯 Project Results

Successfully created:

* 5,000 customer records
* 100 product records
* 50,000 order records
* Optimized PostgreSQL database
* Automated ETL pipeline
* Interactive business intelligence dashboard

### Outcome

This project simulates a real-world retail analytics environment and demonstrates skills commonly required for:

* Data Analyst
* Business Analyst
* Data Engineer
* Python Developer

---

## 🚀 Future Enhancements

* Customer segmentation analysis
* Product recommendation engine
* Sales forecasting using machine learning
* Real-time dashboard updates
* User authentication system
* Cloud deployment



Author

Puma Maheshwari


## 📌 Note

This project is continuously improving as part of my learning journey in data engineering and backend development.






