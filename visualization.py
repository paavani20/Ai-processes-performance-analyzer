# visualization.py

import streamlit as st
import pandas as pd
import numpy as np
import time
from anomaly_detection import AnomalyDetector
from data_collection import collect_process_data

def run_web_interface():
    st.title('AI-Powered Performance Analyzer')
    st.sidebar.header('Settings')

    # Refresh rate input
    refresh_rate = st.sidebar.slider('Refresh Rate (seconds)', 5, 60, 10)
    start_button = st.sidebar.button('Start Monitoring')

    if start_button:  # Only run monitoring when the button is pressed
        # Initialize the anomaly detector and load the model
        detector = AnomalyDetector()
        detector.load_model()

        while True:
            data = collect_process_data()
            st.subheader('Live Process Data')
            st.write(data)

            # Extract features and convert to numpy array
            try:
                features = data[['CPU', 'Memory', 'Read_Bytes', 'Write_Bytes', 'Threads']].apply(pd.to_numeric, errors='coerce').fillna(0).values
            except Exception as e:
                st.error(f'Error processing features: {e}')
                break

            # Make predictions
            try:
                predictions = detector.predict(features)
                data['Anomaly'] = predictions
                st.write('Anomaly Detection Results')
                st.write(data)
            except Exception as e:
                st.error(f'Prediction Error: {e}')
                break

            # Refresh data
            time.sleep(refresh_rate)


if __name__ == "__main__":
    run_web_interface()
