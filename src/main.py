"""Orchestrates the analytics engineering pipeline."""

import logging
from pyspark.sql import SparkSession

from src.config import LOG_DIR, spark_config
from src.cleaning import DataCleaner
from src.ingestion import IngestionManager
from src.metrics import MetricCalculator
from src.transformations import TransformationManager
from src.validations import ValidationManager
from src.utils import (
    ensure_directory,
    setup_logging,
)


def create_spark_session() -> SparkSession:
    """Create a Spark session configured for local development
    and production parity."""
    return (
        SparkSession.builder.appName(spark_config.app_name)
        .master(spark_config.master)
        .getOrCreate()
    )


def run_pipeline() -> None:
    """Execute the end-to-end pipeline orchestration."""
    ensure_directory(LOG_DIR)
    setup_logging(LOG_DIR)
    logger = logging.getLogger(__name__)

    spark = create_spark_session()
    ingestion_manager = IngestionManager(spark)
    cleaner = DataCleaner()
    transformer = TransformationManager()
    validator = ValidationManager()
    metrics = MetricCalculator()

    logger.info("Starting analytics engineering pipeline.")

    try:
        raw_sources = ingestion_manager.ingest()

        bronze_orders = cleaner.clean_orders(
            raw_sources["orders"],
        )
        bronze_customers = cleaner.clean_customers(
            raw_sources["customers"],
        )
        bronze_marketing = cleaner.clean_marketing_spend(
            raw_sources["marketing_spend"],
        )

        order_fact = transformer.build_order_fact(
            bronze_orders,
            bronze_customers,
        )
        customer_dim = transformer.build_customer_dimension(bronze_customers)
        marketing_fact = transformer.build_marketing_spend_fact(bronze_marketing)

        validator.validate_schema(
            order_fact,
            "order_fact_schema",
        )
        validator.validate_schema(
            customer_dim,
            "customer_dim_schema",
        )
        validator.validate_schema(
            marketing_fact,
            "marketing_fact_schema",
        )

        metrics.calculate_revenue_by_channel(order_fact, marketing_fact)
        metrics.calculate_customer_retention(order_fact)
        metrics.calculate_refund_impact(order_fact)

        logger.info(
            "Pipeline orchestration completed. Verify data outputs "
            "and downstream consumption."
        )
    finally:
        spark.stop()


if __name__ == "__main__":
    run_pipeline()
