# Number Analyzer
# Check the sign, parity and divisibility of an integer.

number = int(input("Enter an integer: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

if number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 3.")

if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")
