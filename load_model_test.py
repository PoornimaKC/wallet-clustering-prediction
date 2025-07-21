import joblib
import pandas as pd

# Load model, scaler, and expected feature list
kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')
feature_columns = joblib.load('features.pkl')

# Sample test input (replace values as needed)
input_data = {
    "num_transactions": 50,
    "total_amount": 1500,
    "avg_transaction_amount": 30,
    "num_deposits": 5,
    "num_borrows": 2,
    "num_repayments": 2,
    "num_redeems": 1,
    "num_liquidations": 0,
    "active_days": 15,
    "days_between_tx": 3
}

# Convert to DataFrame
df = pd.DataFrame([input_data])

# Select and reorder features correctly
df = df[feature_columns]

# Scale the data
scaled = scaler.transform(df)

# Predict
prediction = kmeans.predict(scaled)

# Print result
print(f"Predicted Cluster: {prediction[0]}")
