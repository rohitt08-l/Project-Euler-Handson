total_sum = 0

for num in range(2, 354295):
    digits = str(num)

    power_sum = sum(int(digit) ** 5 for digit in digits)

    if num == power_sum:
        total_sum += num

print("Answer:", total_sum)