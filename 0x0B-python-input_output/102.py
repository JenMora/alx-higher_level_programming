#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_statistics(signal, frame):
    print("\nFinal statistics:")
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)

signal.signal(signal.SIGINT, print_statistics)

try:
    for line in sys.stdin:
        try:
            parts = line.strip().split(" ")
            _, _, _, _, _, status_code, file_size = parts[0], parts[2], parts[4], parts[-2], parts[-1]
            status_code = int(status_code)
            file_size = int(file_size)
            
            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print("File size:", total_file_size)
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")
                print("")

        except ValueError:
            # Skip lines with incorrect format
            pass

except KeyboardInterrupt:
    # Handle keyboard interruption gracefully
    print_statistics(None, None)
