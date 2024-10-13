def encode_message(s):
    # Step 1: Swap characters
    swapped_s = list(s)
    for i in range(0, len(s)-1, 2):
        swapped_s[i], swapped_s[i+1] = swapped_s[i+1], swapped_s[i]
    swapped_s = ''.join(swapped_s)

    # Step 2: Replace characters
    char_map = {chr(i): chr(122 - i + 97) for i in range(97, 123)}  # Create a mapping of lowercase English letters to their replacements
    char_map.update({v: k for k, v in char_map.items()})  # Add the original characters as keys with their corresponding values
    encoded_s = ''.join(char_map[c] for c in swapped_s)

    return encoded_s

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    encoded_message = encode_message(S)
    print(encoded_message)