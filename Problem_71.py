#Problem 71
import math

limit = 1_000_000

best_n = 0
best_d = 1

for d in range(1, limit + 1):
    # Get the largest n such that n/d < 3/7
    n = (3 * d - 1) // 7

    # Check if fraction is reduced
    if math.gcd(n, d) == 1:
        # Compare n/d with best_n/best_d without float
        if n * best_d > best_n * d:
            best_n = n
            best_d = d

print("Numerator:", best_n)
print("Fraction:", f"{best_n}/{best_d}")