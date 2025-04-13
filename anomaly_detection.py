from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import joblib

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        self.scaler = StandardScaler()

    def train(self, data):
        scaled_data = self.scaler.fit_transform(data)
        self.model.fit(scaled_data)
        joblib.dump((self.model, self.scaler), 'anomaly_model.joblib')

    def load_model(self):
        self.model, self.scaler = joblib.load('anomaly_model.joblib')

    def predict(self, data):
        scaled_data = self.scaler.transform(data)
        return self.model.predict(scaled_data)