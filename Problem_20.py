import math
# Step 1: Calculate 100!
factorial_100 = math.factorial(100)
digits = str(factorial_100)
digit_sum = sum(int(d) for d in digits)
print(f"The sum of the digits in 100! is: {digit_sum}")