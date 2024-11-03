# cook your dish here
# Read the number of rounds
n = int(input())

# Initialize cumulative scores and maximum lead tracking variables
cumulative_score_p1 = 0
cumulative_score_p2 = 0
max_lead = 0
winner = 0

# Process each round
for _ in range(n):
    # Read the scores for the current round
    score_p1, score_p2 = map(int, input().split())
    
    # Update cumulative scores
    cumulative_score_p1 += score_p1
    cumulative_score_p2 += score_p2
    
    # Calculate current lead and determine current leader
    if cumulative_score_p1 > cumulative_score_p2:
        current_lead = cumulative_score_p1 - cumulative_score_p2
        current_leader = 1
    else:
        current_lead = cumulative_score_p2 - cumulative_score_p1
        current_leader = 2
    
    # Update maximum lead and winner if current lead is the largest so far
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_leader

# Output the winner and the maximum lead
print(winner, max_lead)
