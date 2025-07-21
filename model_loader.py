import joblib

def load_model(path):
    return joblib.load(path)

scaler = load_model("scaler.pkl")
kmeans = load_model("kmeans_model.pkl")
