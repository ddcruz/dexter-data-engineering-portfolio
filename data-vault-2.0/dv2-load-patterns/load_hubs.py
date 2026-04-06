from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from common_utils import insert_new_keys, sha2_from_cols, with_audit_columns


spark = SparkSession.builder.getOrCreate()


def load_hub_policy() -> None:
    src = spark.table("stg_policy")
    df = with_audit_columns(src).select(
        sha2_from_cols("policy_number").alias("hk_policy"),
        F.col("policy_number"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.hub_policy", ["hk_policy"])


def load_hub_claim() -> None:
    src = spark.table("stg_claim")
    df = with_audit_columns(src).select(
        sha2_from_cols("claim_number").alias("hk_claim"),
        F.col("claim_number"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.hub_claim", ["hk_claim"])


def load_hub_claimant() -> None:
    src = spark.table("stg_claimant")
    df = with_audit_columns(src).select(
        sha2_from_cols("claimant_id").alias("hk_claimant"),
        F.col("claimant_id"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.hub_claimant", ["hk_claimant"])


def load_hub_adjuster() -> None:
    src = spark.table("stg_adjuster")
    df = with_audit_columns(src).select(
        sha2_from_cols("adjuster_id").alias("hk_adjuster"),
        F.col("adjuster_id"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.hub_adjuster", ["hk_adjuster"])


def load_hub_claim_line() -> None:
    src = spark.table("stg_claim_line")
    df = with_audit_columns(src).select(
        sha2_from_cols("claim_line_id").alias("hk_claim_line"),
        F.col("claim_line_id"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.hub_claim_line", ["hk_claim_line"])


if __name__ == "__main__":
    load_hub_policy()
    load_hub_claim()
    load_hub_claimant()
    load_hub_adjuster()
    load_hub_claim_line()
