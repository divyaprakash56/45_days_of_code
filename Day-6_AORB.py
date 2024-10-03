# cook your dish here
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    points_A = 500 - 2 * X
    points_B = 1000 - 4 * (X + Y)
    total_points_AB = points_A + points_B
    points_B = 1000 - 4 * Y
    points_A = 500 - 2 * (X + Y)
    total_points_BA = points_B + points_A
    print(max(total_points_AB, total_points_BA))