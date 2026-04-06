CREATE SCHEMA IF NOT EXISTS raw_vault;

CREATE TABLE IF NOT EXISTS raw_vault.sat_policy_details (
  hk_policy STRING NOT NULL,
  hashdiff_policy_details STRING NOT NULL,
  policy_type STRING,
  effective_date DATE,
  expiration_date DATE,
  premium_amount DECIMAL(18,2),
  status STRING,
  eff_start_dts TIMESTAMP NOT NULL,
  eff_end_dts TIMESTAMP,
  is_current BOOLEAN NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.sat_claim_details (
  hk_claim STRING NOT NULL,
  hashdiff_claim_details STRING NOT NULL,
  loss_date DATE,
  report_date DATE,
  claim_status STRING,
  loss_description STRING,
  jurisdiction STRING,
  eff_start_dts TIMESTAMP NOT NULL,
  eff_end_dts TIMESTAMP,
  is_current BOOLEAN NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.sat_claimant_profile (
  hk_claimant STRING NOT NULL,
  hashdiff_claimant_profile STRING NOT NULL,
  claimant_name STRING,
  dob DATE,
  contact_phone STRING,
  address STRING,
  risk_segment STRING,
  eff_start_dts TIMESTAMP NOT NULL,
  eff_end_dts TIMESTAMP,
  is_current BOOLEAN NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.sat_adjuster_profile (
  hk_adjuster STRING NOT NULL,
  hashdiff_adjuster_profile STRING NOT NULL,
  adjuster_name STRING,
  region STRING,
  team STRING,
  license_number STRING,
  assignment_status STRING,
  eff_start_dts TIMESTAMP NOT NULL,
  eff_end_dts TIMESTAMP,
  is_current BOOLEAN NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.sat_claimline_financials (
  hk_claim_line STRING NOT NULL,
  hashdiff_claimline_financials STRING NOT NULL,
  service_code STRING,
  billed_amount DECIMAL(18,2),
  approved_amount DECIMAL(18,2),
  paid_amount DECIMAL(18,2),
  reserve_amount DECIMAL(18,2),
  eff_start_dts TIMESTAMP NOT NULL,
  eff_end_dts TIMESTAMP,
  is_current BOOLEAN NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;
