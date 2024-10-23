# cook your dish here
import math

def minimum_attacks_needed(T, test_cases):
    results = []
    for case in test_cases:
        H, X, Y = case
        
        # Strategy 1: Only normal attacks
        normal_attacks_only = math.ceil(H / X)
        
        # Strategy 2: One special attack, then normal attacks
        if H <= Y:
            special_attack_strategy = 1
        else:
            remaining_health = H - Y
            normal_attacks_after_special = math.ceil(remaining_health / X)
            special_attack_strategy = 1 + normal_attacks_after_special
        
        # The minimum of both strategies
        results.append(min(normal_attacks_only, special_attack_strategy))
    
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get the results
results = minimum_attacks_needed(T, test_cases)

# Output results
for result in results:
    print(result)
