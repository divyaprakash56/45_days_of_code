# cook your dish here
# Read the number of test cases
T = int(input())  

for _ in range(T):
    # Read the tastiness values of the four ingredients
    a, b, c, d = map(int, input().split())
    
    # Calculate the possible tastiness values for the dish
    dishes = [a + c, a + d, b + c, b + d]
    
    # Output the maximum tastiness value
    print(max(dishes))
