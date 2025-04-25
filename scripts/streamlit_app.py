import snowflake.connector
import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Load credentials
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = "MART"
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

# Query data
query = """
    SELECT
        gender,
        product_id,
        brand_name,
        title,
        current_price,
        previous_price,
        colour,
        currency,
        rrp,
        product_code,
        product_type
    FROM ANALYTICS.MART."fct_all_products"
"""

df = pd.read_sql(query, conn)
conn.close()

# Normalize column names to lowercase
df.columns = [col.lower() for col in df.columns]

# Streamlit UI
st.set_page_config(page_title="Fashion Product Dashboard", layout="wide")
st.title("🛍️ Fashion Products Explorer")

# Sidebar filters
st.sidebar.header("🔍 Filters")

genders = ["All"] + sorted(df['gender'].dropna().unique())
selected_gender = st.sidebar.selectbox("Select Gender", genders)

brands = ["All"] + sorted(df['brand_name'].dropna().unique())
selected_brand = st.sidebar.selectbox("Select Brand", brands)

product_types = ["All"] + sorted(df['product_type'].dropna().unique())
selected_type = st.sidebar.selectbox("Select Product Type", product_types)

max_price = float(df['current_price'].max())
selected_price = st.sidebar.slider("Max Price", 0.0, max_price, max_price)

# Apply filters
filtered_df = df.copy()

if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["gender"] == selected_gender]

if selected_brand != "All":
    filtered_df = filtered_df[filtered_df["brand_name"] == selected_brand]

if selected_type != "All":
    filtered_df = filtered_df[filtered_df["product_type"] == selected_type]

filtered_df = filtered_df[filtered_df["current_price"] <= selected_price]

# KPIs
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

col1.metric("🧺 Total Products", f"{filtered_df.shape[0]:,}")
col2.metric("💰 Avg Price", f"${filtered_df['current_price'].mean():.2f}")
col3.metric("🏷️ Unique Brands", f"{filtered_df['brand_name'].nunique()}")
col4.metric("🚻 Selected Gender", selected_gender if selected_gender != "All" else "Both")

st.markdown("---")

# Data Table
st.subheader("🧾 Filtered Product List")
st.dataframe(filtered_df, use_container_width=True)
