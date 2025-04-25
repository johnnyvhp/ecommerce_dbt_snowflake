SELECT
    product_id,
    brand_name,
    title,
    current_price,
    previous_price,
    colour,
    currency,
    rrp,
    productCode AS product_code,
    productType AS product_type
FROM {{ source('RAW', 'MEN_FASHION') }}
