item_name = (input("What item did you buy: "))
price = (float(input("What is the price: ")))

quantity = 3
tax_rate = 0.06

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print(f"Subtotal: ${subtotal}, Tax Amount: ${tax_amount}, Total Cost: ${total_cost}")