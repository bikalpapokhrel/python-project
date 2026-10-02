# Shopping Discount Calculator
# Calculate the subtotal, discount and final amount.

name = input("Enter customer name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
member = input("Are you a member (yes/no)? ").strip().lower()

subtotal = price * quantity

if subtotal >= 10000:
    discount_rate = 15
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

if member == "yes" and subtotal >= 5000:
    discount_rate = discount_rate + 5

discount = subtotal * discount_rate / 100
final_amount = subtotal - discount

print(f"Customer name: {name}")
print(f"Subtotal: Rs. {subtotal:.2f}")
print(f"Discount rate: {discount_rate}%")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final amount: Rs. {final_amount:.2f}")
