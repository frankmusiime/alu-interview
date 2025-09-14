#!/usr/bin/python3
"""
# Defines the minOperations function.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to get exactly n 'H' characters in a file
    using only Copy All and Paste operations.

    Args:
        n (int): The target number of characters

    Returns:
        int: Minimum operations, or 0 if n is impossible
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    # Factorize n
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
## ✅ Example Run (0-main.py)
python
Copy code
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 9
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
## ✅ Expected Output
bash
Copy code
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
Min number of operations to reach 9 characters: 6
## 🔹 Explanation:

n = 4 → factors = 2 × 2 → 2 + 2 = 4 operations

n = 12 → factors = 2 × 2 × 3 → 2 + 2 + 3 = 7 operations

n = 9 → factors = 3 × 3 → 3 + 3 = 6 operations