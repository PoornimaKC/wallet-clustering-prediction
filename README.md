# Wallet Clustering Prediction

This project involves building a clustering model to group crypto wallet users based on their behavior using transaction data. The project includes data cleaning, feature engineering, model building using KMeans, and deploying a Streamlit web application for cluster prediction.

## 🔍 Objective
The objective is to segment wallets into distinct clusters based on features like:
- Wallet balance
- Transaction count
- Average transaction amount
- Number of deposits, borrows, repayments, redeems, liquidations
- Active days

These insights can help DeFi platforms or analysts better understand user behaviors.

## 📁 Dataset
The dataset was provided in CSV format with anonymized crypto wallet transaction details over a period of time. It included:
- `WALLET_ID`, `BALANCE`, `TX_COUNT`, `TOTAL_TX_AMOUNT`, `AVG_TX_AMOUNT`, `DEPOSIT_COUNT`, `BORROW_COUNT`, `REPAY_COUNT`, `REDEEM_COUNT`, `LIQUIDATION_COUNT`, `ACTIVE_DAYS`, etc.

## 🧪 Exploratory Data Analysis (EDA)
- Checked for nulls, zeroes, duplicates
- Distribution analysis for numeric features

## 🛠 Feature Engineering
- Derived meaningful features like `AVG_TX_AMOUNT = TOTAL_TX_AMOUNT / TX_COUNT`
- Normalized features using MinMaxScaler for KMeans

## 🤖 Model Building
- Used **KMeans Clustering**
- Determined optimal `k` using Elbow Method and Silhouette Score → **k=3**
- Trained final model on full dataset and saved using joblib (`kmeans_model.pkl`)

## 🚀 Web App Deployment
Built a Streamlit web app that takes the following inputs:
- Wallet balance
- Total transactions
- Avg. transaction amount
- Counts of deposits, borrows, repayments, redeems, liquidations
- Active days

It predicts and displays the **wallet cluster label (0/1/2)**.

## 📂 Project Structure
📁 wallet_clustering
├── 📄 analysis.md
├── 📄 README.md
├── 📄 app.py
├── 📄 kmeans_model.pkl
├── 📄 scaler.pkl
├── 📄 processed_data.csv
├── 📄 clustering_output.csv
├── 📊 images/ (EDA plots, Elbow curve, etc.)
├── 📄 tracker_table.xlsx

## 🛠 Technologies Used
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Streamlit
- Joblib (model serialization)

## 👤 Author
Poornima KC  
LinkedIn: https://www.linkedin.com/in/poornimakc/ | GitHub: https://github.com/PoornimaKC

