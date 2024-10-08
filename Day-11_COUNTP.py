T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    total_sum = sum(A)
    odd_count = sum(1 for x in A if x % 2 != 0)
    if total_sum % 2 == 0 and odd_count > 0:
        print("YES")
    else:
        print("NO")