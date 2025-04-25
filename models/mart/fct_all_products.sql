WITH men_products AS (
    SELECT
        'Men' AS gender,
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
    FROM {{ ref('fct_unique_men_products') }}
),

woman_products AS (
    SELECT
        'Women' AS gender,
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
    FROM {{ ref('fct_unique_woman_products') }}
)

SELECT * FROM men_products
UNION ALL
SELECT * FROM woman_products
