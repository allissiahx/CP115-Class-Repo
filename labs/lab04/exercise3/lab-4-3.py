hours = float(input())
if hours < 2:
    parkingFee = 0
else:
    if hours < 6:
        parkingFee = hours - 2 * 2
    else:
        if hours > 5:
            parkingFee = hours - 2 * 2 + hours - 5 * 3
print(parkingFee)
