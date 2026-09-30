# Program to calculate selling price of a book

cost_price = float(input("Enter cost price of book: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (cost_price * discount) / 100
selling_price = cost_price - discount_amount

print("Discount Amount =", discount_amount)
print("Selling Price =", selling_price)