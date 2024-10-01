A,B,C,X=map(int,input().split())
if 1 <= A <= 10 and 1 <= B <= 10 and 1 <= C <= 10 and 1 <= X <= 10 and A!=B and B!=C and A!=C:
    if A==X:
        print('yes')
    elif B==X:
        print('yes')
    elif C==X:
        print('YES')
    else:
        print('NO')