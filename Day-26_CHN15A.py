def mutated_minions(test_cases):
    results = []
    for case in test_cases:
        N, K = case['N'], case['K']
        characteristic_values = case['values']
        count = 0
        for value in characteristic_values:
            if (value + K) % 7 == 0:
                count += 1
        results.append(count)
    return results

# Reading input and printing each result on a new line
T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    values = list(map(int, input().split()))
    test_cases.append({'N': N, 'K': K, 'values': values})

results = mutated_minions(test_cases)
for result in results:
    print(result)
