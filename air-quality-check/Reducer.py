#!/usr/bin/env python3
import sys

# Define the CO2 threshold for flagging
CO2_THRESHOLD = 400.0

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    current_room = None
    total_co2 = 0.0
    count = 0
    max_co2 = float('-inf')
    min_co2 = float('inf')
    high_co2_count = 0

    for line in read_input(sys.stdin):
        # Parse the input
        try:
            room_id, co2_value = line.split("\t")
            co2_value = float(co2_value.strip())
        except ValueError:
            continue  # Skip invalid lines

        # Handle data for the current room
        if current_room and room_id != current_room:
            # Output the result for the current room
            high_co2_percentage = (high_co2_count / count) * 100
            status = "Needs Attention" if high_co2_percentage > 10 else "Good"
            print(f"{current_room}\t{total_co2/count:.2f}\t{max_co2:.2f}\t{min_co2:.2f}\t{high_co2_percentage:.2f}\t{status}")

            # Reset for the next room
            total_co2 = 0.0
            count = 0
            max_co2 = float('-inf')
            min_co2 = float('inf')
            high_co2_count = 0

        # Update room-specific statistics
        current_room = room_id
        total_co2 += co2_value
        count += 1
        max_co2 = max(max_co2, co2_value)
        min_co2 = min(min_co2, co2_value)
        if co2_value > CO2_THRESHOLD:
            high_co2_count += 1

    # Output the last room's result
    if current_room:
        high_co2_percentage = (high_co2_count / count) * 100
        status = "Needs Attention" if high_co2_percentage > 10 else "Good"
        print(f"{current_room}\t{total_co2/count:.2f}\t{max_co2:.2f}\t{min_co2:.2f}\t{high_co2_percentage:.2f}\t{status}")

if __name__ == "__main__":
    main()
