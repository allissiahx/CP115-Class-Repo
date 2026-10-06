number = int(input())
score = 0
ignored = 0

while number != 0:
    if score > number: 
        ignored += 1
        number = int(input())
        continue
    score += number
    number = int(input())

print(score)
print(ignored)
