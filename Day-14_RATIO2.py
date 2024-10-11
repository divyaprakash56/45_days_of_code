T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if Y >= 2*X:
        print(0)
    elif X >= 2*Y:
        print(0)
    else:
        diff1 = abs(X - 2*Y)
        diff2 = abs(Y - 2*X)
        print(min(diff1 // 2 + (diff1 % 2), diff2 // 2 + (diff2 % 2)))