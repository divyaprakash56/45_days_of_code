# cook your dish here
import math

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    rounds = int(math.log2(n))
    total_time = rounds * a + (rounds - 1) * b
    print(total_time)
