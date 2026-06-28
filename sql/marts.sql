-- marts.sql
-- SQL definitions for semantic marts and gold-layer aggregations.

-- Customer dimension
CREATE OR REPLACE VIEW dim_customer AS
SELECT *
FROM stg_customers
;

-- Order fact table
CREATE OR REPLACE VIEW fact_order AS
SELECT *
FROM stg_orders
;

-- Marketing spend fact table
CREATE OR REPLACE VIEW fact_marketing_spend AS
SELECT *
FROM stg_marketing_spend
;
