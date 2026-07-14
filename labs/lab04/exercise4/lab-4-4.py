weight = float(input())
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    if weight > 15:
        finalPrice = (weight - 15) * 4 + ticketPrice
    else:
        finalPrice = ticketPrice
print(finalPrice)

