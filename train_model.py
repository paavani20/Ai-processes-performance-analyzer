# train_model.py

from anomaly_detection import AnomalyDetector
from data_collection import collect_process_data
import numpy as np
import pandas as pd  # Added this line to import pandas

if __name__ == "__main__":
    # Collect current process data
    data = collect_process_data()

    # Select only numeric columns and convert to numpy array
    features = data[['CPU', 'Memory', 'Read_Bytes', 'Write_Bytes', 'Threads']].apply(pd.to_numeric, errors='coerce').fillna(0).values

    # Initialize and train the anomaly detector
    detector = AnomalyDetector()
    detector.train(features)

    print("✅ Model trained and saved successfully as 'anomaly_model.joblib'.")
