totalKwh = float(input())
if totalKwh <= 100:
    totalBill = totalKwh * 0.3
else:
    if totalKwh < 200:
        totalBill = totalKwh * 0.5
    else:
        totalBill = totalKwh * 0.75
print(totalBill)
