import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch credentials from env
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the CSVs using full paths
men_fashion_path = os.path.join(BASE_DIR, 'data', 'archive', 'Asosmenfashion.csv')
women_fashion_path = os.path.join(BASE_DIR, 'data', 'archive', 'AsosWomenfashion.csv')

# Read CSVs into DataFrames
men_fashion_df = pd.read_csv(men_fashion_path)
women_fashion_df = pd.read_csv(women_fashion_path)

# Replace NaNs with None for Snowflake compatibility
men_fashion_df = men_fashion_df.where(pd.notnull(men_fashion_df), None)
women_fashion_df = women_fashion_df.where(pd.notnull(women_fashion_df), None)

# Convert DataFrames to list of tuples
men_rows = [tuple(None if pd.isna(x) else x for x in row) for _, row in men_fashion_df.iterrows()]
women_rows = [tuple(None if pd.isna(x) else x for x in row) for _, row in women_fashion_df.iterrows()]

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

cursor = conn.cursor()

# Create MEN_FASHION table
cursor.execute("""
CREATE OR REPLACE TABLE RAW.MEN_FASHION (
    product_id NUMBER,
    brand_name STRING,
    title STRING,
    current_price FLOAT,
    previous_price FLOAT,
    colour STRING,
    currency STRING,
    rrp FLOAT,
    productCode STRING,
    productType STRING
)
""")

# Create WOMAN_FASHION table
cursor.execute("""
CREATE OR REPLACE TABLE RAW.WOMAN_FASHION (
    product_id NUMBER,
    brand_name STRING,
    title STRING,
    current_price FLOAT,
    previous_price FLOAT,
    colour STRING,
    currency STRING,
    rrp FLOAT,
    productCode STRING,
    productType STRING
)
""")

# Bulk insert MEN_FASHION data
cursor.executemany("""
    INSERT INTO RAW.MEN_FASHION (
        product_id, brand_name, title, current_price, previous_price,
        colour, currency, rrp, productCode, productType
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", men_rows)

# Bulk insert WOMAN_FASHION data
cursor.executemany("""
    INSERT INTO RAW.WOMAN_FASHION (
        product_id, brand_name, title, current_price, previous_price,
        colour, currency, rrp, productCode, productType
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", women_rows)

print("All data successfully loaded into Snowflake.")

# Close connections
cursor.close()
conn.close()
