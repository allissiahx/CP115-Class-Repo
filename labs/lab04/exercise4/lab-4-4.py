weight = float(input())
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    finalPrice = (weight * 4) + ticketPrice
print(finalPrice)
