import pandas as pd
import numpy as np

class Anomaly:
    def __init__(self):
        self.log_folder = "anomaly_logs/"

    def check_anomaly(self, device_id, path):
        df = pd.read_csv(path)

        Q1 = df['Power Consumption (kWh)'].quantile(0.25)
        Q3 = df['Power Consumption (kWh)'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        anomalies = df[(df['Power Consumption (kWh)'] < lower_bound) | (df['Power Consumption (kWh)'] > upper_bound)]

        repeated_values = df[df['Power Consumption (kWh)'].duplicated(keep=False)]
        anomalies = pd.concat([anomalies, repeated_values]).drop_duplicates()

        results = []
        for _, row in anomalies.iterrows():
            results.append((device_id, row['Date'], row['Power Consumption (kWh)']))

        return results

    def save_to_log(self, device_id, results):
        log_path = f"{self.log_folder}{device_id}_anomalies.txt"
        
        with open(log_path, "a") as file:
            for device_id, date, power in results:
                file.write(f"{device_id},{date},{power}\n")
