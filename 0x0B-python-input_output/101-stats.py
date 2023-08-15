import sys
import signal

# Define a signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Dictionary to store status code counts
status_code_counts = {}

# Variable to track total file size
total_file_size = 0

# Variable to track the line count
line_count = 0

# Function to print metrics
def print_metrics():
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts.keys()):
        print("{}: {}".format(status_code, status_code_counts[status_code]))

# Read input from stdin
try:
    for line in sys.stdin:
        try:
            _, _, _, _, status_code_str, file_size_str = line.split('"')[2].split()
            status_code = int(status_code_str)
            file_size = int(file_size_str)
            
            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics()

        except ValueError:
            pass

except KeyboardInterrupt:
    print_metrics()

