#!/bin/bash

# Run cicflowmeter to capture traffic and save it to the flows.csv file
python src/network_sniffer.py &

# remove the checkpoint file if it exists
rm -f traffic_data/last_processed_checkpoint.ckpt

# Run the Python script for anomaly detection
python src/anomaly_detection_script.py
