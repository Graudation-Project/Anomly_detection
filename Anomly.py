import pandas as pd
import numpy as np

class Anomaly:
    def __init__(self):
        self.log_path = "anomaly_log.txt"

    def check_anomaly(self, device_id, path):
        df = pd.read_csv(path)

        mean = df['Power Consumption (kWh)'].mean()
        std = df['Power Consumption (kWh)'].std()

        df['Z-Score'] = (df['Power Consumption (kWh)'] - mean) / std

        anomalies_df = df[(df['Z-Score'] > 3) | (df['Z-Score'] < -3)]

        results = []
        for _, row in anomalies_df.iterrows():
            results.append((device_id, row['Date'], row['Power Consumption (kWh)']))

        return results

    def save_to_log(self, results):
        with open(self.log_path, "a") as f:
            for device_id, date, power in results:
                f.write(f"{device_id},{date},{power}\n")