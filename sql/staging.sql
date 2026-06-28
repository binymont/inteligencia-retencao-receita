-- staging.sql
-- SQL definitions for staging tables and temporary views.

-- Example staging for orders
CREATE OR REPLACE VIEW stg_orders AS
SELECT *
FROM bronze.orders
;

-- Example staging for customers
CREATE OR REPLACE VIEW stg_customers AS
SELECT *
FROM bronze.customers
;

-- Example staging for marketing spend
CREATE OR REPLACE VIEW stg_marketing_spend AS
SELECT *
FROM bronze.marketing_spend
;
