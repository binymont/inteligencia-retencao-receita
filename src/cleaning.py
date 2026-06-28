"""Cleaning routines for raw and bronze data layers."""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class DataCleaner:
    """Encapsulates data quality and standardization operations."""

    def clean_orders(self, orders_df: DataFrame) -> DataFrame:
        """Prepare and standardize orders data."""
        return orders_df

    def clean_customers(self, customers_df: DataFrame) -> DataFrame:
        """Prepare and standardize customers data."""
        return customers_df

    def clean_marketing_spend(self, marketing_df: DataFrame) -> DataFrame:
        """Prepare and standardize marketing spend data."""
        return marketing_df
