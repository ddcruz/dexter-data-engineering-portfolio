CREATE SCHEMA IF NOT EXISTS raw_vault;

CREATE TABLE IF NOT EXISTS raw_vault.lnk_claim_policy (
  hk_lnk_claim_policy STRING NOT NULL,
  hk_claim STRING NOT NULL,
  hk_policy STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.lnk_claim_claimant (
  hk_lnk_claim_claimant STRING NOT NULL,
  hk_claim STRING NOT NULL,
  hk_claimant STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.lnk_claim_adjuster (
  hk_lnk_claim_adjuster STRING NOT NULL,
  hk_claim STRING NOT NULL,
  hk_adjuster STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;

CREATE TABLE IF NOT EXISTS raw_vault.lnk_claimline_claim (
  hk_lnk_claimline_claim STRING NOT NULL,
  hk_claim_line STRING NOT NULL,
  hk_claim STRING NOT NULL,
  load_dts TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
)
USING DELTA;
