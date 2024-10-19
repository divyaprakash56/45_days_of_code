# cook your dish here
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    limak_eaten, bob_eaten, turn = 0, 0, 1
    
    while True:
        if turn % 2 == 1:
            if limak_eaten + turn > A:
                print("Bob")
                break
            limak_eaten += turn
        else:
            if bob_eaten + turn > B:
                print("Limak")
                break
            bob_eaten += turn
        turn += 1
