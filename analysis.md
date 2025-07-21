# Wallet Clustering - Analysis Report

## 📌 Objective
To group crypto wallets into behavioral clusters using KMeans clustering on features derived from their transaction patterns and balances.

---

## 🔎 Dataset Summary
The dataset contains transactional records of wallets, including:
- `BALANCE`, `TX_COUNT`, `TOTAL_TX_AMOUNT`, `DEPOSIT_COUNT`, etc.

---

## 📊 EDA Summary
- Missing values: None
- Most wallets are moderately active with low liquidation/redeem counts

---

## 💡 Feature Engineering
- `AVG_TX_AMOUNT = TOTAL_TX_AMOUNT / TX_COUNT`
- Dropped identifiers like `WALLET_ID`
- Scaled features using MinMaxScaler

---

## 🔁 Model Details
- Chose **KMeans Clustering** as unsupervised learning algorithm
- Found `k=3` optimal from Elbow Curve and Silhouette score
- Model was trained on the cleaned, scaled dataset

---

## 📈 Cluster Insights
- **Cluster 0**: High balance, high transactions – possibly whales or high-volume users
- **Cluster 1**: Moderate users with regular deposits and repayments
- **Cluster 2**: Low activity, fewer transactions – possibly inactive or dormant wallets

---

## 🔮 Streamlit Prediction App
- Accepts user input (wallet metrics)
- Predicts the cluster using the saved model and scaler
- Output: Cluster 0 / 1 / 2

---

## ✅ Conclusion
The wallet clustering model successfully groups wallets into actionable segments. This can aid targeted marketing, fraud detection, and personalized DeFi service offerings.

