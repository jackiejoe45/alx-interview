#!/usr/bin/python3
"""
This module contains a function that determines
if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
    data (list): List of integers representing bytes.

    Returns:
    bool: True if data is valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Check the leading bits to determine how many bytes are expected
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 1 byte
                continue
            elif (byte >> 5) == 0b110:  # 2 bytes
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3 bytes
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4 bytes
                num_bytes = 3
            else:
                return False  # Invalid leading byte
        else:
            # Expecting continuation bytes
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0  # All bytes must be accounted for
