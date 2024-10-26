# cook your dish here
def can_wear_glove(fingers, sheaths):
    n = len(fingers)
    
    # Check the 'front' orientation
    front = all(fingers[i] <= sheaths[i] for i in range(n))
    
    # Check the 'back' orientation
    back = all(fingers[i] <= sheaths[n - i - 1] for i in range(n))
    
    # Determine the result based on possible orientations
    if front and back:
        return "both"
    elif front:
        return "front"
    elif back:
        return "back"
    else:
        return "none"

# Main input handling
t = int(input().strip())
results = []

for _ in range(t):
    n = int(input().strip())
    fingers = list(map(int, input().strip().split()))
    sheaths = list(map(int, input().strip().split()))
    
    result = can_wear_glove(fingers, sheaths)
    results.append(result)

# Print all results
print("\n".join(results))
