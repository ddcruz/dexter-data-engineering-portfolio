from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def norm_col(column_name: str):
    """Normalize values before hashing to keep keys deterministic across loads."""
    return F.upper(F.trim(F.coalesce(F.col(column_name).cast("string"), F.lit(""))))


def sha2_from_cols(*column_names: str):
    normalized = [norm_col(c) for c in column_names]
    return F.sha2(F.concat_ws("||", *normalized), 256)


def with_audit_columns(df: DataFrame, load_col: str = "extract_dts") -> DataFrame:
    return (
        df.withColumn("load_dts", F.col(load_col).cast("timestamp"))
        .withColumn("record_source", F.col("record_source"))
    )


def insert_new_keys(df: DataFrame, target_table: str, key_columns: list[str]) -> None:
    existing = df.sparkSession.table(target_table).select(*key_columns).dropDuplicates()
    new_rows = df.join(existing, key_columns, "left_anti")
    new_rows.write.mode("append").saveAsTable(target_table)
