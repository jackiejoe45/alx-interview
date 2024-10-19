#!/usr/bin/python3
"""
This module returns the minimum number of operations
needed to copy a string n times
"""


def minOperations(n):
    """
    This function returns the minimum number of operations
    needed to copy a string n times
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
