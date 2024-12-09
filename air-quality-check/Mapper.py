#!/usr/bin/env python3
import os
import sys

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    # Extract room ID from the folder structure
    current_dir = os.getenv('map_input_file', '')  # Hadoop provides the file path via this environment variable
    room_id = current_dir.split('/')[-2]  # Assumes room folder structure is iot-sensor-data/IOT/<room_id>/

    for line in read_input(sys.stdin):
        # Skip empty lines
        if not line:
            continue

        try:
            timestamp, co2_value = line.split(",")
            co2_value = float(co2_value.strip())
            print(f"{room_id}\t{co2_value}")
        except ValueError:
            # Log the error or handle invalid lines if needed
            continue

if __name__ == "__main__":
    main()
