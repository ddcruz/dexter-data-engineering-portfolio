-- 1) Duplicate key checks (should return 0 rows per query)
SELECT hk_policy, COUNT(*) AS cnt FROM raw_vault.hub_policy GROUP BY hk_policy HAVING COUNT(*) > 1;
SELECT hk_claim, COUNT(*) AS cnt FROM raw_vault.hub_claim GROUP BY hk_claim HAVING COUNT(*) > 1;
SELECT hk_claimant, COUNT(*) AS cnt FROM raw_vault.hub_claimant GROUP BY hk_claimant HAVING COUNT(*) > 1;
SELECT hk_adjuster, COUNT(*) AS cnt FROM raw_vault.hub_adjuster GROUP BY hk_adjuster HAVING COUNT(*) > 1;
SELECT hk_claim_line, COUNT(*) AS cnt FROM raw_vault.hub_claim_line GROUP BY hk_claim_line HAVING COUNT(*) > 1;

-- 2) Link integrity checks (should return 0 rows)
SELECT l.hk_claim
FROM raw_vault.lnk_claim_policy l
LEFT JOIN raw_vault.hub_claim h ON l.hk_claim = h.hk_claim
WHERE h.hk_claim IS NULL;

SELECT l.hk_policy
FROM raw_vault.lnk_claim_policy l
LEFT JOIN raw_vault.hub_policy h ON l.hk_policy = h.hk_policy
WHERE h.hk_policy IS NULL;

SELECT l.hk_claimant
FROM raw_vault.lnk_claim_claimant l
LEFT JOIN raw_vault.hub_claimant h ON l.hk_claimant = h.hk_claimant
WHERE h.hk_claimant IS NULL;

SELECT l.hk_adjuster
FROM raw_vault.lnk_claim_adjuster l
LEFT JOIN raw_vault.hub_adjuster h ON l.hk_adjuster = h.hk_adjuster
WHERE h.hk_adjuster IS NULL;

SELECT l.hk_claim_line
FROM raw_vault.lnk_claimline_claim l
LEFT JOIN raw_vault.hub_claim_line h ON l.hk_claim_line = h.hk_claim_line
WHERE h.hk_claim_line IS NULL;

-- 3) Satellite current-row uniqueness (should return 0 rows)
SELECT hk_policy, COUNT(*) AS current_rows
FROM raw_vault.sat_policy_details
WHERE is_current = true
GROUP BY hk_policy
HAVING COUNT(*) > 1;

SELECT hk_claim, COUNT(*) AS current_rows
FROM raw_vault.sat_claim_details
WHERE is_current = true
GROUP BY hk_claim
HAVING COUNT(*) > 1;

SELECT hk_claimant, COUNT(*) AS current_rows
FROM raw_vault.sat_claimant_profile
WHERE is_current = true
GROUP BY hk_claimant
HAVING COUNT(*) > 1;

SELECT hk_adjuster, COUNT(*) AS current_rows
FROM raw_vault.sat_adjuster_profile
WHERE is_current = true
GROUP BY hk_adjuster
HAVING COUNT(*) > 1;

SELECT hk_claim_line, COUNT(*) AS current_rows
FROM raw_vault.sat_claimline_financials
WHERE is_current = true
GROUP BY hk_claim_line
HAVING COUNT(*) > 1;
