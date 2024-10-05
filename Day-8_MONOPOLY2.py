# cook your dish here
T = int(input())
results = []

for _ in range(T):
    # Read profits for companies A, B, C, D
    P, Q, R, S = map(int, input().split())

    if (P > Q + R + S) or (Q > P + R + S) or (R > P + Q + S) or (S > P + Q + R):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))
