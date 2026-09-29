number = int(input())
count = 0
num1 = 0
difference = 0
biggest_jump = 0

while number != 0:
    count += 1
    num1= number
    number = int(input())
    difference = number-num1
    if difference > biggest_jump:
        biggest_jump = difference
   


print(count)
print(biggest_jump)
