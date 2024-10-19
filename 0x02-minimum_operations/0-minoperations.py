#!/usr/bin/python3
"""
This module returns the minimum number of operations needed to copy a string n times
"""


def minOperations(x):
    """
    This function returns the minimum number of operations needed to copy a string n times
    """
    currentNumber = x
    numberOfOperations = 1
    if (x <= 0):
        return 0
    while (currentNumber != 1):
        if (isprime(currentNumber)):
            numberOfOperations = currentNumber
            currentNumber += 1
            break
        if (currentNumber%2 == 0):
            numberOfOperations+=2
            currentNumber /=2
            break
        if (currentNumber%2 != 0):
            numberOfOperations+=1
            currentNumber -=1
            break
    return numberOfOperations


def isprime(n):
    """
    This function checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True
