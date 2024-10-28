# cook your dish here
def min_cost_to_buy_jewels(test_cases):
    results = []
    for jewels in test_cases:
        jewel_count = {}
        
        # Count occurrences of each jewel
        for jewel in jewels:
            if jewel in jewel_count:
                jewel_count[jewel] += 1
            else:
                jewel_count[jewel] = 1
                
        # Calculate cost
        cost = 0
        for count in jewel_count.values():
            cost += (count + 1) // 2  # Buy half + 1 if odd
        
        results.append(cost)
    return results

# Reading input
T = int(input())
test_cases = [input().strip() for _ in range(T)]

# Getting results
results = min_cost_to_buy_jewels(test_cases)

# Printing results for each test case
for result in results:
    print(result)
