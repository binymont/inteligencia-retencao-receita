"""Data ingestion layer for the analytics engineering pipeline."""

from typing import Dict

from pyspark.sql import DataFrame, SparkSession

from src.config import RAW_DIR, CSV_SOURCES
from src.utils import ensure_directory


class IngestionManager:
    """Manages ingestion of raw data into the Bronze layer."""

    def __init__(self, spark: SparkSession) -> None:
        self.spark = spark

    def load_csv(self, source_name: str, file_name: str) -> DataFrame:
        """Load a CSV file from raw data and return a DataFrame."""
        file_path = RAW_DIR / file_name
        return (
            self.spark.read.options(
                header=True,
                inferSchema=True,
                mode="PERMISSIVE",
                timestampFormat="yyyy-MM-dd HH:mm:ss",
            )
            .csv(
                str(file_path),
            )
        )

    def ingest(self) -> Dict[str, DataFrame]:
        """Ingest configured raw CSV sources into memory
        for downstream processing."""
        ensure_directory(RAW_DIR)
        loaded_data = {}
        for source_name, file_name in CSV_SOURCES.items():
            loaded_data[source_name] = self.load_csv(
                source_name,
                file_name,
            )
        return loaded_data
