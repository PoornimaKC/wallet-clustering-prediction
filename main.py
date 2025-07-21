from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model and scaler
try:
    kmeans = joblib.load("kmeans_model.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    kmeans = None
    scaler = None

# Define input schema with 10 features
class WalletFeatures(BaseModel):
    balance: float
    num_transactions: int
    total_amount: float
    avg_transaction_amount: float
    num_deposits: int
    num_borrows: int
    num_repayments: int
    num_redeems: int
    num_liquidations: int
    active_days: int

@app.post("/predict_cluster")
def predict_cluster(data: WalletFeatures):
    try:
        if kmeans is None or scaler is None:
            return {"error": "Model or Scaler not loaded."}

        features = np.array([[
            data.balance,
            data.num_transactions,
            data.total_amount,
            data.avg_transaction_amount,
            data.num_deposits,
            data.num_borrows,
            data.num_repayments,
            data.num_redeems,
            data.num_liquidations,
            data.active_days
        ]])

        scaled_features = scaler.transform(features)
        predicted_cluster = kmeans.predict(scaled_features)[0]
        return {"predicted_cluster": int(predicted_cluster)}

    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}
