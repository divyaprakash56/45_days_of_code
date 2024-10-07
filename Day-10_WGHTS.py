def can_measure_weight(W, X, Y, Z):
    # Check all combinations
    return (W == X or 
            W == Y or 
            W == Z or 
            W == X + Y or 
            W == X + Z or 
            W == Y + Z or 
            W == X + Y + Z)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        W, X, Y, Z = map(int, data[i].split())
        if can_measure_weight(W, X, Y, Z):
            results.append("YES")
        else:
            results.append("NO")
    
    # Print results
    print("\n".join(results))

if __name__ == "__main__":
    main()

