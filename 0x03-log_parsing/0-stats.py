#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys
import re
from typing import Dict, Union


def print_statistics(total_size: int, status_codes: Dict[str, int]) -> None:
    """
    Print the current statistics
    Args:
        total_size: Total file size
        status_codes: Dictionary of status codes and their counts
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")


def main():
    """Main function to process the log files"""
    total_size = 0
    line_count = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    # Regular expression pattern for log line validation
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'

    try:
        for line in sys.stdin:
            try:
                match = re.match(pattern, line.strip())
                if match:
                    status_code = match.group(1)
                    file_size = int(match.group(2))

                    # Update metrics
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    total_size += file_size
                    line_count += 1

                    # Print statistics every 10 lines
                    if line_count % 10 == 0:
                        print_statistics(total_size, status_codes)

            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        # Handle CTRL+C
        print_statistics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()