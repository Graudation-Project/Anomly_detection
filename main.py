from Anomly import Anomaly
Machines = {
    "1A0": "1A0.csv",
    "1B0": "1B0.csv",
    "1C0": "1C0.csv",
    "1D0": "1D0.csv",
    "1E0": "1E0.csv"
}




if __name__ == "__main__":
    anomaly_checker = Anomaly()
    for id in Machines:
        results = anomaly_checker.check_anomaly(id, Machines[id])
    anomaly_checker.save_to_log(results)
    print("Anomaly detection completed. Check anomaly_log.txt for results.")