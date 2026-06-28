-- quality_checks.sql
-- Data quality checks for staging and gold layers.

-- Example null check
SELECT
    'orders' AS source,
    COUNT(*) AS total_rows,
    SUM(CASE WHEN order_id IS NULL THEN 1 ELSE 0 END) AS null_order_id
FROM bronze.orders
;

-- Example consistency check
SELECT
    'marketing_spend' AS source,
    COUNT(*) AS total_rows,
    SUM(CASE WHEN spend_amount < 0 THEN 1 ELSE 0 END) AS invalid_spend_amount
FROM bronze.marketing_spend
;
