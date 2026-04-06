from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from delta.tables import DeltaTable

from common_utils import sha2_from_cols, with_audit_columns


spark = SparkSession.builder.getOrCreate()


def upsert_satellite(
    source_df,
    target_table: str,
    parent_key_col: str,
    hashdiff_col: str,
    payload_cols: list[str],
):
    current = spark.table(target_table).filter(F.col("is_current") == True)

    staged = (
        source_df.alias("s")
        .join(
            current.select(parent_key_col, hashdiff_col).alias("c"),
            on=[parent_key_col],
            how="left",
        )
        .filter((F.col(f"c.{hashdiff_col}").isNull()) | (F.col(f"c.{hashdiff_col}") != F.col(f"s.{hashdiff_col}")))
        .select("s.*")
    )

    if staged.limit(1).count() == 0:
        return

    delta_target = DeltaTable.forName(spark, target_table)

    # End-date previous current row when payload changes.
    delta_target.alias("t").merge(
        staged.alias("s"),
        f"t.{parent_key_col} = s.{parent_key_col} AND t.is_current = true",
    ).whenMatchedUpdate(
        condition=f"t.{hashdiff_col} <> s.{hashdiff_col}",
        set={"eff_end_dts": F.col("s.eff_start_dts"), "is_current": F.lit(False)},
    ).execute()

    staged.write.mode("append").saveAsTable(target_table)


def load_sat_policy_details() -> None:
    src = with_audit_columns(spark.table("stg_policy"))
    df = src.select(
        sha2_from_cols("policy_number").alias("hk_policy"),
        sha2_from_cols("policy_type", "effective_date", "expiration_date", "premium_amount", "status").alias(
            "hashdiff_policy_details"
        ),
        F.col("policy_type"),
        F.col("effective_date").cast("date"),
        F.col("expiration_date").cast("date"),
        F.col("premium_amount").cast("decimal(18,2)"),
        F.col("status"),
        F.col("load_dts").alias("eff_start_dts"),
        F.lit(None).cast("timestamp").alias("eff_end_dts"),
        F.lit(True).alias("is_current"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    upsert_satellite(df, "raw_vault.sat_policy_details", "hk_policy", "hashdiff_policy_details", ["policy_type", "effective_date", "expiration_date", "premium_amount", "status"])


def load_sat_claim_details() -> None:
    src = with_audit_columns(spark.table("stg_claim"))
    df = src.select(
        sha2_from_cols("claim_number").alias("hk_claim"),
        sha2_from_cols("loss_date", "report_date", "claim_status", "loss_description", "jurisdiction").alias(
            "hashdiff_claim_details"
        ),
        F.col("loss_date").cast("date"),
        F.col("report_date").cast("date"),
        F.col("claim_status"),
        F.col("loss_description"),
        F.col("jurisdiction"),
        F.col("load_dts").alias("eff_start_dts"),
        F.lit(None).cast("timestamp").alias("eff_end_dts"),
        F.lit(True).alias("is_current"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    upsert_satellite(df, "raw_vault.sat_claim_details", "hk_claim", "hashdiff_claim_details", ["loss_date", "report_date", "claim_status", "loss_description", "jurisdiction"])


def load_sat_claimant_profile() -> None:
    src = with_audit_columns(spark.table("stg_claimant"))
    df = src.select(
        sha2_from_cols("claimant_id").alias("hk_claimant"),
        sha2_from_cols("claimant_name", "dob", "contact_phone", "address", "risk_segment").alias(
            "hashdiff_claimant_profile"
        ),
        F.col("claimant_name"),
        F.col("dob").cast("date"),
        F.col("contact_phone"),
        F.col("address"),
        F.col("risk_segment"),
        F.col("load_dts").alias("eff_start_dts"),
        F.lit(None).cast("timestamp").alias("eff_end_dts"),
        F.lit(True).alias("is_current"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    upsert_satellite(df, "raw_vault.sat_claimant_profile", "hk_claimant", "hashdiff_claimant_profile", ["claimant_name", "dob", "contact_phone", "address", "risk_segment"])


def load_sat_adjuster_profile() -> None:
    src = with_audit_columns(spark.table("stg_adjuster"))
    df = src.select(
        sha2_from_cols("adjuster_id").alias("hk_adjuster"),
        sha2_from_cols("adjuster_name", "region", "team", "license_number", "assignment_status").alias(
            "hashdiff_adjuster_profile"
        ),
        F.col("adjuster_name"),
        F.col("region"),
        F.col("team"),
        F.col("license_number"),
        F.col("assignment_status"),
        F.col("load_dts").alias("eff_start_dts"),
        F.lit(None).cast("timestamp").alias("eff_end_dts"),
        F.lit(True).alias("is_current"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    upsert_satellite(df, "raw_vault.sat_adjuster_profile", "hk_adjuster", "hashdiff_adjuster_profile", ["adjuster_name", "region", "team", "license_number", "assignment_status"])


def load_sat_claimline_financials() -> None:
    src = with_audit_columns(spark.table("stg_claim_line"))
    df = src.select(
        sha2_from_cols("claim_line_id").alias("hk_claim_line"),
        sha2_from_cols("service_code", "billed_amount", "approved_amount", "paid_amount", "reserve_amount").alias(
            "hashdiff_claimline_financials"
        ),
        F.col("service_code"),
        F.col("billed_amount").cast("decimal(18,2)"),
        F.col("approved_amount").cast("decimal(18,2)"),
        F.col("paid_amount").cast("decimal(18,2)"),
        F.col("reserve_amount").cast("decimal(18,2)"),
        F.col("load_dts").alias("eff_start_dts"),
        F.lit(None).cast("timestamp").alias("eff_end_dts"),
        F.lit(True).alias("is_current"),
        F.col("load_dts"),
        F.col("record_source"),
    )
    upsert_satellite(df, "raw_vault.sat_claimline_financials", "hk_claim_line", "hashdiff_claimline_financials", ["service_code", "billed_amount", "approved_amount", "paid_amount", "reserve_amount"])


if __name__ == "__main__":
    load_sat_policy_details()
    load_sat_claim_details()
    load_sat_claimant_profile()
    load_sat_adjuster_profile()
    load_sat_claimline_financials()
