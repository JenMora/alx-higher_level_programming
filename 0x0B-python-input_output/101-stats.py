#!/usr/bin/python3
import sys
from collections import defaultdict
"""
initialize variables to store metrics
"""


total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        _, _, _, _, _, status_code, file_size = line.strip().split(" ")
        status_code = int(status_code)
        file_ssize = int(file_ssize)

        total_file_size += file_ssize
        status_code_counts[status_code] += 1
        line_count += 1

    if line_count % 10 == 0:
        print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
        print("")

except: KeyboardInterrupt

print("\nFinal statistics:")
print("Total file size:", total_file_size)
for code in sorted(status_code_counts.keys()):
    print(f"{code}: {status_code_counts[code]}")
