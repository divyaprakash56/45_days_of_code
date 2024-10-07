def calculate_minimum_masks(N, A):
    # Calculate the number of uninfected people
    U = N - A
    
    # To stop the spread, either mask all infected or all uninfected people
    return min(A, U)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    T = int(data[0])  # Number of test cases
    results = []
    
    for i in range(1, T + 1):
        N, A = map(int, data[i].split())
        
        # Calculate the minimum masks required for each case
        min_masks = calculate_minimum_masks(N, A)
        results.append(min_masks)
    
    # Output the results for all test cases
    for result in results:
        print(result)

if __name__ == "__main__":
    main()