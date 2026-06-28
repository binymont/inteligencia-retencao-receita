"""Configuration definitions for revenue retention intelligence pipeline."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"

RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

CSV_SOURCES: Dict[str, str] = {
    "orders": "orders.csv",
    "customers": "customers.csv",
    "marketing_spend": "marketing_spend.csv",
}


@dataclass(frozen=True)
class SparkConfig:
    app_name: str = "revenue_retention_intelligence"
    master: str = "local[*]"
    shuffle_partitions: int = 8
    checkpoint_dir: Path = PROJECT_ROOT / "checkpoints"


spark_config = SparkConfig()
