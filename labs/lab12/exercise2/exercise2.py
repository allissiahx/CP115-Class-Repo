num = 1

while num <= 100:
    if (num % 7) == 0 and (num % 13) == 0:
        found_number = num
        break
    num += 1


print(found_number)
