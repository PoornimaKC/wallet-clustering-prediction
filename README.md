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

## 🧩 Workflow
1. **Data ingestion**: Load and parse `user_wallet_transactions.json`.  
2. **Feature engineering**: Aggregate into wallet-level metrics (transaction counts, deposit/borrow behavior, durations, etc.).  
3. **Rule‑based scoring**: Optional step to derive numeric scores from features.  
4. **Model‑based segmentation**: StandardScaling + K‑Means clustering to assign risk groups.  
5. **API & UI**:
   - FastAPI serves model endpoint `/predict_cluster`.
   - Streamlit app provides user GUI for predictions.
6. **Testing**: `load_model_test.py` confirms model loading and prediction.  
7. **Reporting**: `analysis.md` segment interpretations.

It predicts and displays the **wallet cluster label (0/1/2)**.

## 🗂 Files Included
- `wallet_level_dataset.csv`: Wallet features  
- `kmeans_model.pkl`, `scaler.pkl`, `features.pkl`: Trained models  
- `clustered_wallets.csv`: Final scored & labeled wallets  
- `main.py`: FastAPI backend  
- `streamlit_app.py`: Streamlit frontend  
- `load_model_test.py`: Model-connectivity test  
- `README.md`, `analysis.md`: Documentation

 ## 🚀 Run Instructions
### Setup  
```bash
conda env create --file environment.yml  
conda activate fastapi_project

### Run API
```bash
cd fastapi_project
uvicorn main:app --reload

### Run Streamlit UI (in separate terminal)
```bash
streamlit run streamlit_app.py

### Test API from notebook or terminal
```bash
python load_model_test.py

## 🛠 Technologies Used
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Streamlit
- Joblib (model serialization)

Regards,
Poornima KC  
LinkedIn: https://www.linkedin.com/in/poornimakc/ | GitHub: https://github.com/PoornimaKC

