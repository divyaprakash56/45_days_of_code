# cook your dish here
def can_complete_assignments(test_cases):
    results = []
    for X in test_cases:
        if X <= 7:
            results.append("Yes")
        else:
            results.append("No")
    return results

T = int(input())
test_cases = [int(input()) for _ in range(T)]

results = can_complete_assignments(test_cases)

for result in results:
    print(result)
