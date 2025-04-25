# ecommerce_dbt_snowflake

## 📚 Project Overview

This project simulates a real-world data pipeline for an e-commerce dataset.  
The goal was to build a complete data transformation flow using modern tools:
- Data ingestion into Snowflake
- Data transformation and modeling using dbt
- Data visualization using Streamlit (future step)

The project follows best practices for scalable, production-grade data architecture.

---

## 🏗️ Architecture

| Layer | Technology | Description |
|------|------------|-------------|
| Ingestion | Python + Snowflake | Load raw CSV files into Snowflake |
| Staging | dbt (Snowflake) | Clean and normalize raw data |
| Marts | dbt (Snowflake) | Create final analytics tables |
| Visualization | Streamlit | Build interactive dashboards (coming soon) |

---

## ⚙️ Tech Stack

- **Snowflake** (cloud data warehouse)
- **dbt Cloud** (data transformations and testing)
- **Python** (data ingestion scripts)
- **GitHub** (version control and collaboration)
- **Streamlit** (dashboard and visualization, WIP)

---

## 📂 Project Structure

```bash
models/
  staging/
    stg_men_fashion.sql
    sources.yml
  marts/
    fct_unique_men_products.sql
    fct_unique_men_products.yml
macros/
  generate_schema_name.sql
scripts/
  load_to_snowflake.py
dbt_project.yml
README.md
```

---

## 📊 Current dbt Models

| Model | Description |
|------|-------------|
| `stg_men_fashion` | Cleans the MEN_FASHION raw data |
| `fct_unique_men_products` | Deduplicated final products table with one row per product_id |

✅ All models tested for `not_null` constraints where appropriate.


---

## 🧐 Key Learnings

- How to organize a real-world data project using Snowflake and dbt
- Schema design best practices (`RAW → STAGING → MART`)
- Data modeling and transformation
- Building analytics-ready tables

---

