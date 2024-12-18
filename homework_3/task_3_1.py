import sys
from math_package.math import ListOperations

# Example
numbers = [-3.0, 1, 2, *(False, 8), '8.8']

try:
    result = ListOperations.sum(numbers)
    print(f"Elements sum: {result}")
except Exception as e:
    error_type = repr(sys.exc_info()[0]).split(r"'")[1]
    print(f"{error_type} caught: {e}")
