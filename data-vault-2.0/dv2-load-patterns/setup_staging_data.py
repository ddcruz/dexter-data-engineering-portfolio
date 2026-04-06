from pyspark.sql import SparkSession
from pyspark.sql import functions as F


spark = SparkSession.builder.getOrCreate()


def load_synthetic_staging_data() -> None:
    """Create a small synthetic insurance-claims dataset in staging tables."""

    stg_policy_rows = [
        {
            "policy_number": "POL-1001",
            "policy_type": "AUTO",
            "effective_date": "2025-01-01",
            "expiration_date": "2025-12-31",
            "premium_amount": 1250.50,
            "status": "ACTIVE",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "policy_number": "POL-1002",
            "policy_type": "HOME",
            "effective_date": "2025-03-01",
            "expiration_date": "2026-02-28",
            "premium_amount": 980.00,
            "status": "ACTIVE",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "policy_number": "POL-1003",
            "policy_type": "AUTO",
            "effective_date": "2024-06-01",
            "expiration_date": "2025-05-31",
            "premium_amount": 1430.75,
            "status": "LAPSED",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
    ]

    stg_claim_rows = [
        {
            "claim_number": "CLM-9001",
            "policy_number": "POL-1001",
            "claimant_id": "CLT-501",
            "adjuster_id": "ADJ-301",
            "loss_date": "2025-10-15",
            "report_date": "2025-10-16",
            "claim_status": "OPEN",
            "loss_description": "Rear-end collision",
            "jurisdiction": "TX",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "claim_number": "CLM-9002",
            "policy_number": "POL-1002",
            "claimant_id": "CLT-502",
            "adjuster_id": "ADJ-302",
            "loss_date": "2025-11-05",
            "report_date": "2025-11-06",
            "claim_status": "OPEN",
            "loss_description": "Kitchen water damage",
            "jurisdiction": "FL",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "claim_number": "CLM-9003",
            "policy_number": "POL-1001",
            "claimant_id": "CLT-503",
            "adjuster_id": "ADJ-301",
            "loss_date": "2025-12-10",
            "report_date": "2025-12-12",
            "claim_status": "CLOSED",
            "loss_description": "Windshield crack",
            "jurisdiction": "TX",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
    ]

    stg_claimant_rows = [
        {
            "claimant_id": "CLT-501",
            "claimant_name": "Jordan Mills",
            "dob": "1988-04-12",
            "contact_phone": "555-0101",
            "address": "120 Oak St, Austin, TX",
            "risk_segment": "STANDARD",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "claimant_id": "CLT-502",
            "claimant_name": "Priya Shah",
            "dob": "1991-09-03",
            "contact_phone": "555-0102",
            "address": "88 Lake Dr, Miami, FL",
            "risk_segment": "PREFERRED",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "claimant_id": "CLT-503",
            "claimant_name": "Marco Ruiz",
            "dob": "1979-01-20",
            "contact_phone": "555-0103",
            "address": "42 Elm Ave, Dallas, TX",
            "risk_segment": "STANDARD",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
    ]

    stg_adjuster_rows = [
        {
            "adjuster_id": "ADJ-301",
            "adjuster_name": "Avery Bennett",
            "region": "South",
            "team": "Auto Claims",
            "license_number": "TX-77811",
            "assignment_status": "ACTIVE",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "adjuster_id": "ADJ-302",
            "adjuster_name": "Nina Patel",
            "region": "Southeast",
            "team": "Property Claims",
            "license_number": "FL-99128",
            "assignment_status": "ACTIVE",
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
    ]

    stg_claim_line_rows = [
        {
            "claim_line_id": "CLL-7001",
            "claim_number": "CLM-9001",
            "service_code": "AUTO_REPAIR",
            "billed_amount": 2100.00,
            "approved_amount": 1850.00,
            "paid_amount": 1850.00,
            "reserve_amount": 0.00,
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "claim_line_id": "CLL-7002",
            "claim_number": "CLM-9002",
            "service_code": "WATER_REMED",
            "billed_amount": 5200.00,
            "approved_amount": 4700.00,
            "paid_amount": 2000.00,
            "reserve_amount": 2700.00,
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
        {
            "claim_line_id": "CLL-7003",
            "claim_number": "CLM-9003",
            "service_code": "GLASS_REPAIR",
            "billed_amount": 450.00,
            "approved_amount": 400.00,
            "paid_amount": 400.00,
            "reserve_amount": 0.00,
            "record_source": "synthetic_seed_v1",
            "extract_dts": "2026-01-15 09:00:00",
        },
    ]

    spark.createDataFrame(stg_policy_rows).withColumn(
        "extract_dts", F.to_timestamp("extract_dts")
    ).withColumn("effective_date", F.to_date("effective_date")).withColumn(
        "expiration_date", F.to_date("expiration_date")
    ).write.mode("overwrite").format("delta").saveAsTable("stg_policy")

    spark.createDataFrame(stg_claim_rows).withColumn(
        "extract_dts", F.to_timestamp("extract_dts")
    ).withColumn("loss_date", F.to_date("loss_date")).withColumn(
        "report_date", F.to_date("report_date")
    ).write.mode("overwrite").format("delta").saveAsTable("stg_claim")

    spark.createDataFrame(stg_claimant_rows).withColumn(
        "extract_dts", F.to_timestamp("extract_dts")
    ).withColumn("dob", F.to_date("dob")).write.mode("overwrite").format("delta").saveAsTable(
        "stg_claimant"
    )

    spark.createDataFrame(stg_adjuster_rows).withColumn(
        "extract_dts", F.to_timestamp("extract_dts")
    ).write.mode("overwrite").format("delta").saveAsTable("stg_adjuster")

    spark.createDataFrame(stg_claim_line_rows).withColumn(
        "extract_dts", F.to_timestamp("extract_dts")
    ).write.mode("overwrite").format("delta").saveAsTable("stg_claim_line")


if __name__ == "__main__":
    load_synthetic_staging_data()
    print("Synthetic staging tables created: stg_policy, stg_claim, stg_claimant, stg_adjuster, stg_claim_line")
