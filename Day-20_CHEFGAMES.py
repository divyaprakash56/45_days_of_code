# cook your dish here
t = int(input())
for _ in range(t):
    r = list(map(int, input().split()))
    if sum(r) == 0:
        print("IN")
    else:
        print("OUT")
