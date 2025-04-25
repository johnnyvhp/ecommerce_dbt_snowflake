import streamlit as st
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables (Snowflake credentials)
load_dotenv()

# Snowflake connection
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database="ANALYTICS",
    schema="MART"
)

# Query the data
query = """
    SELECT
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
    FROM FCT_UNIQUE_MEN_PRODUCTS
"""
df = pd.read_sql(query, conn)

# Streamlit app
st.title("E-commerce Men's Fashion Products")

# Filters
brand = st.selectbox("Select a brand", options=["All"] + list(df['brand_name'].dropna().unique()))

if brand != "All":
    df = df[df['brand_name'] == brand]

st.dataframe(df)

# Close Snowflake connection
conn.close()
