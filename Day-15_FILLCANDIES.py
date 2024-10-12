# cook your dish here
import math

# Input the number of test cases
T = int(input())

for _ in range(T):
    # Read N (candies), K (pockets per bag), and M (candies per pocket)
    N, K, M = map(int, input().split())
    
    # Calculate the total capacity of one bag
    capacity_per_bag = K * M
    
    # Calculate the minimum number of bags required
    bags_required = math.ceil(N / capacity_per_bag)
    
    # Output the result
    print(bags_required)
