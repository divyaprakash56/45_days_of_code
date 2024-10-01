# cook your dish here
from collections import Counter
import sys

# Read the number of test cases
input = sys.stdin.read
data = input().splitlines()

index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    N = int(data[index])
    index += 1
    A = list(map(int, data[index].split()))
    index += 1
    
    # Count frequencies of each element
    frequency = Counter(A)
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Calculate minimum operations
    min_operations = N - max_freq
    results.append(min_operations)

# Output all results
sys.stdout.write('\n'.join(map(str, results)) + '\n')
