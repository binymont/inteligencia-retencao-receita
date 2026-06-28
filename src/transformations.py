"""Transformation layer for Silver and Gold data models."""

from pyspark.sql import DataFrame


class TransformationManager:
    """Executes reusable data modeling transformations."""

    def build_customer_dimension(self, customers_df: DataFrame) -> DataFrame:
        """Create a customer dimension model from cleansed customers."""
        return customers_df

    def build_order_fact(self, orders_df: DataFrame, customers_df: DataFrame) -> DataFrame:
        """Create an order fact model enriched with customer attributes."""
        return orders_df

    def build_marketing_spend_fact(self, marketing_df: DataFrame) -> DataFrame:
        """Create a marketing spend fact table for channel analysis."""
        return marketing_df
