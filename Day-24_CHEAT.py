# cook your dish here
def count_tuesdays(T, days_list):
    results = []
    for N in days_list:
        if N < 2:
            results.append(0)
        else:
            results.append((N - 2) // 7 + 1)
    return results

# Input reading
T = int(input())
days_list = [int(input()) for _ in range(T)]

# Get results and output
results = count_tuesdays(T, days_list)
for result in results:
    print(result)
