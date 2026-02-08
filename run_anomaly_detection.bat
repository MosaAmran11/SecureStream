@REM Run cicflowmeter to capture traffic and save it to the flows.csv file
py src\network_sniffer.py

@REM remove the checkpoint file if it exists
del /f traffic_data\last_processed_checkpoint.ckpt

@REM Run the Python script for anomaly detection
py src\anomaly_detection_script.py
