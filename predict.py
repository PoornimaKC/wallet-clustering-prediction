import numpy as np
from models.model_loader import scaler, kmeans

def predict_cluster(data):
    arr = np.array([list(data.values())])
    scaled = scaler.transform(arr)
    cluster = kmeans.predict(scaled)
    return int(cluster[0])
