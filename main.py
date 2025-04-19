import pandas as pd
from Anomaly import Anomaly

machines = {
    "1A0": "1A0.csv",
    "1B0": "1B0.csv",
    "1C0": "1C0.csv",
    "1D0": "1D0.csv",
    "1E0": "1E0.csv"
}

anomaly_checker = Anomaly()

for device_id, file_path in machines.items():
    results = anomaly_checker.check_anomaly(device_id, file_path)
    if results:
        anomaly_checker.save_to_log(device_id, results)
    else:
        print(f"No anomalies found for device {device_id}.")
