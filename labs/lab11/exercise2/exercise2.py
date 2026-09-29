score = int(input())
count = 0
total_a = 0
total_b = 0
winner = 0

while score != -1:
    count += 1
    i = count % 2
    if i == 0:
        total_b += score
    else:
        total_a += score
    score = int (input())

if total_a == total_b:
    winner = "Tie"
elif total_a > total_b:
    winner ="A"
else:
    winner ="B"


print(total_a)
print(total_b)
print(winner)
