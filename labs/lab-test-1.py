weight = int(input())
if weight <= 5:
    totalCharge = weight * 8
else:
    totalCharge = 5 * 8 + (weight - 5) * 6
if totalCharge > 60:
    totalCharge = totalCharge + 10
print(weight)
print(totalCharge)
