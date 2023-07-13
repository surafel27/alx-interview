#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n == 0:
        return 0

    operations = 0
    factors = []

    # Find prime factors of n
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)

    # Calculate the minimum number of operations
    for factor in factors:
        operations += factor

    return operations
