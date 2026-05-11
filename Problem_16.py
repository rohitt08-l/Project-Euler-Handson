# Calculate 2 to the power of 1000
number = 2**1000

# Convert the number to a string and sum each digit
digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)