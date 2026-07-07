annualIncome = float(input())
if annualIncome <= 50000:
    totalTax = annualIncome * 0
else:
    if annualIncome <= 500000:
        totalTax = annualIncome * 1 / 100
    else:
        totalTax = annualIncome * 2 / 100
print(totalTax)
