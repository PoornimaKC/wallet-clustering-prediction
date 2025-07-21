# Wallet Clustering - Analysis Report

## Objective
To group crypto wallets into behavioral clusters using KMeans clustering on features derived from their transaction patterns and balances.

---

## Feature Summary
Wallet-level metrics crafted include:
- Transaction counts and volumes (total, avg)
- Counts per action type (deposits, borrows, repays…)
- Active behavior (days active, gaps between)
  
These encapsulate financial engagement and DeFi protocol diversity.

---

## Scoring & Clustering
- A preliminary numeric credit score (0–1000) assigned via rule-based weighting.
- K‑Means clustering (k=3) on behavioral features revealed:
  - **Cluster 0 (“Medium Risk”)**: Mid-level transactions and activity  
  - **Cluster 1 (“High Risk”)**: Large volumes but fewer interactions/activities  
  - **Cluster 2 (“Low Risk”)**: Frequent, varied activity — higher engagement and reliability
 
---

## Score Distributions
- Majority fall in **Medium Risk** cluster (~60–70%)
- Smaller proportions in **Low** and **High Risk**
- Pattern: wallets with higher active days and transaction diversity cluster into **Low Risk**

---

## Interpretation & Insights
- **Low Risk** wallets: exhibit consistent interaction, diversified DeFi usage, longevity
- **High Risk** wallets: high volumes but less frequent engagement — could be whales or bots
- **Medium Risk**: average usage — typical retail or mixed users

---

## Next Steps
- Tune clusters (e.g. k=4 or other features like asset diversity, session behavior)
- Compare to supervised scores if labeled data becomes available
- Deploy as microservice in cloud environment

