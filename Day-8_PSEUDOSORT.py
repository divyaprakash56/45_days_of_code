def is_pseudo_sorted(arr):
    n = len(arr)
    violations = []

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            violations.append(i)

    if not violations:
        return "YES"

    if len(violations) > 1:
        return "NO"

    i = violations[0]

    arr[i], arr[i + 1] = arr[i + 1], arr[i]


    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            return "NO"
    
    return "YES"


T = int(input())
results = []

for _ in range(T):
    N = int(input()) 
    A = list(map(int, input().split()))  
    results.append(is_pseudo_sorted(A))

print("\n".join(results))
