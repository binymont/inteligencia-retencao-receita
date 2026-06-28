"""Metric definitions and analytics abstractions for the pipeline."""

from pyspark.sql import DataFrame


class MetricCalculator:
    """Holds metric calculation methods for the Gold layer."""

    def calculate_revenue_by_channel(
        self,
        order_fact_df: DataFrame,
        marketing_fact_df: DataFrame,
    ) -> DataFrame:
        """Define the interface to compute revenue attribution by marketing channel."""
        return order_fact_df

    def calculate_customer_retention(
        self,
        order_fact_df: DataFrame,
    ) -> DataFrame:
        """Define the interface to compute retention and churn indicators."""
        return order_fact_df

    def calculate_refund_impact(
        self,
        order_fact_df: DataFrame,
    ) -> DataFrame:
        """Define the interface to compute cancellation and refund impact."""
        return order_fact_df
