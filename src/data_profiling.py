"""Exploratory profiling utilities for raw CSV datasets."""

import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple

from pyspark.sql import DataFrame, SparkSession, functions as F, types as T

from src.config import RAW_DIR

logger = logging.getLogger(__name__)


def create_spark_session(app_name: str = "data_profiling") -> SparkSession:
    spark = SparkSession.builder.appName(app_name).master("local[*]").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    logger.info("Spark session inicializada para data profiling.")
    return spark


def discover_csvs(raw_dir: Path = RAW_DIR) -> List[Path]:
    if not raw_dir.exists():
        logger.warning("Diretório raw não existe: %s", raw_dir)
        return []

    csv_files = sorted(raw_dir.glob("*.csv"))
    logger.info("Foram identificados %d arquivos CSV em %s", len(csv_files), raw_dir)
    return csv_files


def load_csv(spark: SparkSession, path: Path) -> DataFrame:
    logger.info("Lendo CSV: %s", path)
    return (
        spark.read.option("header", "true")
        .option("inferSchema", "true")
        .option("mode", "PERMISSIVE")
        .csv(str(path))
    )


def get_schema_info(df: DataFrame) -> List[Tuple[str, str, bool]]:
    schema_info = [(field.name, field.dataType.simpleString(), field.nullable) for field in df.schema]
    logger.debug("Schema detectado: %s", schema_info)
    return schema_info


def count_rows(df: DataFrame) -> int:
    rows = df.count()
    logger.info("Quantidade de registros: %d", rows)
    return int(rows)


def count_columns(df: DataFrame) -> int:
    columns = len(df.columns)
    logger.info("Quantidade de colunas: %d", columns)
    return columns


def count_nulls(df: DataFrame) -> Dict[str, int]:
    exprs = [
        F.count(F.when(F.col(column).isNull() | (F.col(column) == ""), column)).alias(column)
        for column in df.columns
    ]
    row = df.select(exprs).collect()[0].asDict()
    null_counts = {column: int(row[column]) for column in df.columns}
    logger.info("Nulos por coluna: %s", null_counts)
    return null_counts


def count_duplicates(df: DataFrame) -> int:
    total_rows = df.count()
    distinct_rows = df.distinct().count()
    duplicates = total_rows - distinct_rows
    logger.info("Duplicados: %d", duplicates)
    return int(duplicates)


def describe_numeric(df: DataFrame) -> Dict[str, Dict[str, float]]:
    numeric_fields = [
        field.name
        for field in df.schema
        if isinstance(
            field.dataType,
            (T.ByteType, T.ShortType, T.IntegerType, T.LongType, T.FloatType, T.DoubleType, T.DecimalType),
        )
    ]
    if not numeric_fields:
        logger.info("Nenhuma coluna numérica detectada.")
        return {}

    description = df.select(*numeric_fields).describe().collect()
    result: Dict[str, Dict[str, float]] = {
        field: {} for field in numeric_fields
    }
    for row in description:
        summary = row["summary"]
        for field in numeric_fields:
            value = row[field]
            result[field][summary] = float(value) if value is not None else 0.0
    logger.info("Estatísticas descritivas numéricas geradas para: %s", numeric_fields)
    return result


def detect_primary_keys(df: DataFrame) -> List[str]:
    row_count = df.count()
    candidates: List[str] = []
    for column in df.columns:
        distinct_count = df.select(column).distinct().count()
        if distinct_count == row_count:
            candidates.append(column)
    logger.info("Candidatas a chave primária: %s", candidates)
    return candidates


def detect_relationships(tables: List[Dict[str, Any]]) -> List[Tuple[str, str, str, float]]:
    relationships: List[Tuple[str, str, str, float]] = []
    for left in tables:
        for right in tables:
            if left["source"] == right["source"]:
                continue
            left_df = left["dataframe"]
            right_df = right["dataframe"]
            shared_columns = set(left_df.columns).intersection(right_df.columns)
            for column in shared_columns:
                left_distinct = left_df.select(column).distinct().count()
                if left_distinct == 0:
                    continue
                intersection = (
                    left_df.select(column)
                    .distinct()
                    .join(right_df.select(column).distinct(), column, "inner")
                    .count()
                )
                coverage = intersection / left_distinct
                if coverage >= 0.8:
                    relationships.append(
                        (left["source"], right["source"], column, coverage)
                    )
                    logger.info(
                        "Detectado relacionamento possível: %s.%s -> %s.%s (%.2f)",
                        left["source"],
                        column,
                        right["source"],
                        column,
                        coverage,
                    )
    return relationships


def collect_profile(df: DataFrame, source_name: str) -> Dict[str, Any]:
    schema = get_schema_info(df)
    profile: Dict[str, Any] = {
        "source": source_name,
        "schema": schema,
        "row_count": count_rows(df),
        "column_count": count_columns(df),
        "null_counts": count_nulls(df),
        "duplicates": count_duplicates(df),
        "numeric_statistics": describe_numeric(df),
        "candidate_primary_keys": detect_primary_keys(df),
        "column_types": {name: dtype for name, dtype, _ in schema},
        "dataframe": df,
    }
    return profile


def generate_data_profile_report(
    profiles: List[Dict[str, Any]],
    relationships: List[Tuple[str, str, str, float]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines: List[str] = ["# Data Profile Report", "", "## Resumo Geral", ""]
    total_records = sum(profile["row_count"] for profile in profiles)
    lines.append(f"Quantidade de arquivos: {len(profiles)}")
    lines.append(f"Quantidade de tabelas: {len(profiles)}")
    lines.append(f"Quantidade total de registros: {total_records}")
    lines.append("")

    if not profiles:
        lines.append("Nenhum arquivo CSV encontrado em data/raw no momento.")
    else:
        for profile in profiles:
            lines.append(f"## Tabela: {profile['source']}")
            lines.append(f"- Registros: {profile['row_count']}")
            lines.append(f"- Colunas: {profile['column_count']}")
            lines.append(f"- Possíveis chaves primárias: {profile['candidate_primary_keys']}")
            lines.append(f"- Duplicados: {profile['duplicates']}")
            lines.append("")
            lines.append("### Schema")
            for name, dtype, nullable in profile["schema"]:
                lines.append(f"- `{name}`: `{dtype}` | Nullable: {nullable}")
            lines.append("")
            lines.append("### Tipos de Coluna")
            for name, dtype in profile["column_types"].items():
                lines.append(f"- `{name}`: `{dtype}`")
            lines.append("")
            lines.append("### Valores Nulos")
            for column, null_count in profile["null_counts"].items():
                lines.append(f"- `{column}`: {null_count}")
            lines.append("")
            lines.append("### Estatísticas Descritivas Numéricas")
            if profile["numeric_statistics"]:
                for column, stats in profile["numeric_statistics"].items():
                    lines.append(f"- `{column}`:")
                    for metric, value in stats.items():
                        lines.append(f"  - {metric}: {value}")
            else:
                lines.append("- Nenhuma coluna numérica detectada.")
            lines.append("")

        lines.append("## Relacionamentos Possíveis")
        if relationships:
            for left, right, column, coverage in relationships:
                lines.append(
                    f"- `{left}.{column}` pode se relacionar com `{right}.{column}` "
                    f"(cobertura {coverage:.2f})"
                )
        else:
            lines.append("- Nenhum relacionamento automático identificado entre as tabelas.")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Relatório de data profiling gerado em %s", output_path)


def run_data_profiling() -> None:
    spark = create_spark_session()
    try:
        csv_paths = discover_csvs()
        profiles: List[Dict[str, Any]] = []

        for csv_path in csv_paths:
            df = load_csv(spark, csv_path)
            profile = collect_profile(df, csv_path.stem)
            profiles.append(profile)

        relationships = detect_relationships(profiles)
        generate_data_profile_report(
            profiles,
            relationships,
            Path("docs/data_profile_report.md"),
        )
    finally:
        spark.stop()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    run_data_profiling()
