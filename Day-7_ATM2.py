# cook your dish here
def atm_withdrawals(test_cases):
    results = []
    for n, k, requests in test_cases:
        result = []
        for amount in requests:
            if amount <= k:
                result.append('1') 
                k -= amount         
            else:
                result.append('0') 
        results.append(''.join(result))  
    return results

T = int(input())
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    requests = list(map(int, input().split()))
    test_cases.append((N, K, requests))

results = atm_withdrawals(test_cases)

for result in results:
    print(result)
