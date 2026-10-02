# Electricity Bill Calculator
# Calculate charges separately for each electricity slab.

units = float(input("Enter units consumed: "))

if units < 0:
    print(f"Invalid units: {units}. Enter zero or more.")
else:
    if units <= 20:
        bill = units * 5
    elif units <= 50:
        bill = (20 * 5) + ((units - 20) * 7)
    elif units <= 100:
        bill = (20 * 5) + (30 * 7) + ((units - 50) * 10)
    else:
        bill = (20 * 5) + (30 * 7) + (50 * 10)
        bill = bill + ((units - 100) * 12)

    print(f"Units consumed: {units:g}")
    print(f"Total bill: Rs. {bill:.2f}")
