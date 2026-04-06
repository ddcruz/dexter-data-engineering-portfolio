from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from common_utils import insert_new_keys, sha2_from_cols, with_audit_columns


spark = SparkSession.builder.getOrCreate()


def load_lnk_claim_policy() -> None:
    src = with_audit_columns(spark.table("stg_claim"))
    df = src.select(
        sha2_from_cols("claim_number", "policy_number").alias("hk_lnk_claim_policy"),
        sha2_from_cols("claim_number").alias("hk_claim"),
        sha2_from_cols("policy_number").alias("hk_policy"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.lnk_claim_policy", ["hk_lnk_claim_policy"])


def load_lnk_claim_claimant() -> None:
    src = with_audit_columns(spark.table("stg_claim"))
    df = src.select(
        sha2_from_cols("claim_number", "claimant_id").alias("hk_lnk_claim_claimant"),
        sha2_from_cols("claim_number").alias("hk_claim"),
        sha2_from_cols("claimant_id").alias("hk_claimant"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.lnk_claim_claimant", ["hk_lnk_claim_claimant"])


def load_lnk_claim_adjuster() -> None:
    src = with_audit_columns(spark.table("stg_claim"))
    df = src.select(
        sha2_from_cols("claim_number", "adjuster_id").alias("hk_lnk_claim_adjuster"),
        sha2_from_cols("claim_number").alias("hk_claim"),
        sha2_from_cols("adjuster_id").alias("hk_adjuster"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.lnk_claim_adjuster", ["hk_lnk_claim_adjuster"])


def load_lnk_claimline_claim() -> None:
    src = with_audit_columns(spark.table("stg_claim_line"))
    df = src.select(
        sha2_from_cols("claim_line_id", "claim_number").alias("hk_lnk_claimline_claim"),
        sha2_from_cols("claim_line_id").alias("hk_claim_line"),
        sha2_from_cols("claim_number").alias("hk_claim"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    insert_new_keys(df, "raw_vault.lnk_claimline_claim", ["hk_lnk_claimline_claim"])


if __name__ == "__main__":
    load_lnk_claim_policy()
    load_lnk_claim_claimant()
    load_lnk_claim_adjuster()
    load_lnk_claimline_claim()
