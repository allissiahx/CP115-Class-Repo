sales = int(input())
count = 0
record_days = 1

while sales != 0:
    count += 1
    sales1 = sales
    sales = int(input())
    if sales1 < sales:
        record_days += 1

print(count)
print(record_days)
