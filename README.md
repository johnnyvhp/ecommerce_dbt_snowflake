# E-Commerce Pipeline Project (dbt + Snowflake)

This is an end-to-end data engineering project simulating a real-world modern data stack:
- Python is used to load raw CSV data into Snowflake
- dbt is used to model, test, and document the data in warehouse
- Final tables will be visualized using Streamlit dashboards

## Tools Used
- Python 3.x
- Snowflake (Free Tier)
- dbt (CLI)
- Streamlit (TBD)

## Project Structure
- `data/`: CSV files to be loaded
- `scripts/`: Python scripts for data ingestion
- `dbt_project/`: dbt model structure (staging, intermediate, final)
- `notebooks/`: exploratory analysis or dev testing

## Pipeline Flow
CSV → Python → Snowflake (raw) → dbt (staging → final) → Streamlit
