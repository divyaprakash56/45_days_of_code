# cook your dish here
def is_expert(x, y):
   
    approval_percentage = (y / x) * 100
    

    return approval_percentage >= 50


t = int(input())


for _ in range(t):
  
    x, y = map(int, input().split())

    if is_expert(x, y):
        print("YES")
    else:
        print("NO")