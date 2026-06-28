"""Helper utilities for the analytics engineering project."""

import logging
from pathlib import Path
from typing import Dict


def setup_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "pipeline.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def normalize_columns(columns: Dict[str, str]) -> Dict[str, str]:
    """Return a normalized mapping of source column names."""
    return {
        source.lower().strip(): target
        for source, target in columns.items()
    }


def ensure_directory(path: Path) -> Path:
    """Create and return a path ensuring the directory exists."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def infer_data_quality_level(records_count: int, error_count: int) -> str:
    """Infer a simple quality label based on error ratio."""
    return (
        "high"
        if records_count and error_count / records_count < 0.01
        else "medium"
        if records_count
        else "unknown"
    )
