# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

#declare variables for the prices
coffee_price = 3.50
muffin_price = 2.10
water_price = 1.05

#calculate all the total for each item
coffee_total = round(coffee_price * 2, 2)
muffin_total = round(muffin_price * 3, 2)
water_total = round(water_price * 4, 2)

receipt = ("========== RECEIPT ==========")
item = (f"Item\tPrice\tQty\tTotal")
coffee = (f"Coffee\t{coffee_price:.2f}\t2\t${coffee_total:.2f}")
muffin = (f"Muffin\t{muffin_price:.2f}\t3\t${muffin_total:.2f}")
water = (f"Water\t{water_price:.2f}\t4\t${water_total:.2f}")
dot_Line = ("-----------------------------")
ending = ("===============================")


#calculate subtotal, tax and total
subtotal = round(coffee_total + muffin_total + water_total, 2)
tax = round(subtotal * 0.06, 2)
total = round(subtotal + tax, 2)

print(f"{receipt}\n{item}\n{coffee}\n{muffin}\n{water}\n{dot_Line}\nSubtotal\t${subtotal:.2f}\nTax (6%)\t${tax}\nTotal\t\t${total}\n{ending}")
