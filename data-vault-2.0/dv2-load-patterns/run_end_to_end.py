from pathlib import Path

from pyspark.sql import SparkSession

from load_hubs import (
    load_hub_adjuster,
    load_hub_claim,
    load_hub_claim_line,
    load_hub_claimant,
    load_hub_policy,
)
from load_links import (
    load_lnk_claim_adjuster,
    load_lnk_claim_claimant,
    load_lnk_claim_policy,
    load_lnk_claimline_claim,
)
from load_satellites import (
    load_sat_adjuster_profile,
    load_sat_claim_details,
    load_sat_claimant_profile,
    load_sat_claimline_financials,
    load_sat_policy_details,
)
from setup_staging_data import load_synthetic_staging_data


spark = SparkSession.builder.getOrCreate()


def run_sql_file(path: Path) -> None:
    sql_text = path.read_text(encoding="utf-8")
    for statement in [s.strip() for s in sql_text.split(";") if s.strip()]:
        spark.sql(statement)


def run_all() -> None:
    base_dir = Path(__file__).resolve().parents[1]

    run_sql_file(base_dir / "hubs" / "hub_tables.sql")
    run_sql_file(base_dir / "links" / "link_tables.sql")
    run_sql_file(base_dir / "satellites" / "satellite_tables.sql")

    load_synthetic_staging_data()

    load_hub_policy()
    load_hub_claim()
    load_hub_claimant()
    load_hub_adjuster()
    load_hub_claim_line()

    load_lnk_claim_policy()
    load_lnk_claim_claimant()
    load_lnk_claim_adjuster()
    load_lnk_claimline_claim()

    load_sat_policy_details()
    load_sat_claim_details()
    load_sat_claimant_profile()
    load_sat_adjuster_profile()
    load_sat_claimline_financials()

    print("End-to-end run complete. Execute tests/validation_queries.sql next.")


if __name__ == "__main__":
    run_all()
