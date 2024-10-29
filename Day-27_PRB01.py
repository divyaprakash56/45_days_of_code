import math

def is_prime(n):
    if n <= 1:
        return False  # Ensure 1 is not counted as prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3 early
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Input number of test cases
T = int(input())
results = []

# Process each test case
for _ in range(T):
    N = int(input())
    if is_prime(N):
        results.append("yes")
    else:
        results.append("no")

# Print all results line by line
print("\n".join(results))
