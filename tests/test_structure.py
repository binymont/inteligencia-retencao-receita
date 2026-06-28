import os
from pathlib import Path


def test_project_structure() -> None:
    base = Path(__file__).resolve().parents[1]
    expected = [
        "data/raw",
        "data/bronze",
        "data/silver",
        "data/gold",
        "src/ingestion.py",
        "src/cleaning.py",
        "src/transformations.py",
        "src/metrics.py",
        "src/validations.py",
        "src/config.py",
        "src/utils.py",
        "src/main.py",
        "sql/staging.sql",
        "sql/marts.sql",
        "sql/quality_checks.sql",
        "docs/business_discovery.md",
        "docs/architecture.md",
        "docs/data_dictionary.md",
        "docs/dimensional_model.md",
        "docs/executive_report.md",
        "README.md",
        "requirements.txt",
        ".gitignore",
        "LICENSE",
    ]

    for path in expected:
        assert (base / path).exists(), f"Missing expected path: {path}"
