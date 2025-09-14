#!/usr/bin/python3
"""
Module: 0-minoperations
Contains function minOperations(n) that calculates the minimum
number of operations needed to reach exactly n 'H' characters
using only Copy All and Paste.
"""


def minOperations(n):
    """
    Returns the minimum number of operations to get n H's in the file.
    If n is impossible to achieve, returns 0.

    The logic:
    - Use the prime factorization of n.
    - Each factor represents a sequence of Copy All + Paste operations.
    - Add factors to get the total minimum operations.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
