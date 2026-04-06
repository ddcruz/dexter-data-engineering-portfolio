CREATE SCHEMA IF NOT EXISTS raw_vault;

CREATE TABLE IF NOT EXISTS raw_vault.hub_policy (
  hk_policy STRING NOT NULL,
  policy_number STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.hub_claim (
  hk_claim STRING NOT NULL,
  claim_number STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.hub_claimant (
  hk_claimant STRING NOT NULL,
  claimant_id STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.hub_adjuster (
  hk_adjuster STRING NOT NULL,
  adjuster_id STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.hub_claim_line (
  hk_claim_line STRING NOT NULL,
  claim_line_id STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;
