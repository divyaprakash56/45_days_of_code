# cook your dish here
from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    freq = Counter(A)
    max_count = max(freq.values())
    min_moves = N - max_count
    print(min_moves)
