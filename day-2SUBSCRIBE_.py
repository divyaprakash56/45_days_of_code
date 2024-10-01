# cook your dish here
T = int(input())  

for _ in range(T):
    N, X = map(int, input().split())  
    subscriptions_required = N // 6 
    if N % 6 != 0: 
        subscriptions_required += 1
    total_cost = subscriptions_required * X 
    print(total_cost)