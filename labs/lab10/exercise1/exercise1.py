num_rounds = int(input())
rounds_processed = 0 
bonus = 0


for i in range (0, num_rounds):
    rounds_processed += 1
    score = int(input())
    if score > 100:
        bonus = score + (score * 0.2)
    else:
        bonus = score
    final_score += bonus



print(f"{final_score:.1f}")
print(rounds_processed)
