import streamlit as st
import requests

st.title("Wallet Clustering Prediction")

# Input fields (10 total)
balance = st.number_input("Wallet Balance", min_value=0.0, step=100.0)
num_transactions = st.number_input("Number of Transactions", min_value=0, step=1)
total_amount = st.number_input("Total Transaction Amount", min_value=0.0, step=10.0)
avg_transaction_amount = st.number_input("Average Transaction Amount", min_value=0.0, step=10.0)
num_deposits = st.number_input("Number of Deposits", min_value=0, step=1)
num_borrows = st.number_input("Number of Borrows", min_value=0, step=1)
num_repayments = st.number_input("Number of Repayments", min_value=0, step=1)
num_redeems = st.number_input("Number of Redeems", min_value=0, step=1)
num_liquidations = st.number_input("Number of Liquidations", min_value=0, step=1)
active_days = st.number_input("Active Days", min_value=0, step=1)

if st.button("Predict Cluster"):
    payload = {
        "balance": balance,
        "num_transactions": num_transactions,
        "total_amount": total_amount,
        "avg_transaction_amount": avg_transaction_amount,
        "num_deposits": num_deposits,
        "num_borrows": num_borrows,
        "num_repayments": num_repayments,
        "num_redeems": num_redeems,
        "num_liquidations": num_liquidations,
        "active_days": active_days
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict_cluster", json=payload)
        result = response.json()

        if response.status_code == 200 and "predicted_cluster" in result:
            st.success(f"✅ Predicted Wallet Cluster: {result['predicted_cluster']}")
        else:
            st.error(f"⚠️ API Error: {result}")
    except Exception as e:
        st.error(f"❌ Request failed: {e}")
