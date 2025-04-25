WITH ranked_products AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY product_id
            ORDER BY rrp DESC NULLS LAST, current_price DESC NULLS LAST
        ) AS row_num
    FROM {{ ref('stg_woman_fashion') }}
)

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
FROM ranked_products
WHERE row_num = 1
