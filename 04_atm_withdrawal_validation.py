# ATM Withdrawal Validation
# Validate the PIN, withdrawal amount and available balance.

correct_pin = "1234"

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
pin = input("Enter PIN: ")

if pin == correct_pin and amount > 0 and amount <= balance:
    remaining_balance = balance - amount
    print(f"Withdrawal successful.")
    print(f"Amount withdrawn: Rs. {amount}")
    print(f"Remaining balance: Rs. {remaining_balance}")
elif pin != correct_pin:
    print(f"Invalid PIN.")
elif amount <= 0:
    print(f"Invalid withdrawal amount.")
else:
    print(f"Insufficient balance.")
