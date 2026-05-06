def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_consecutive_primes(a, b):
    n = 0
    while True:
        # The formula: n^2 + an + b
        value = n**2 + a*n + b
        if is_prime(value):
            n += 1
        else:
            return n

max_primes = 0
best_a = 0
best_b = 0

# Since n=0 must result in a prime, b must be prime. 
# We can optimize by only checking prime values for b.
primes_under_1000 = [i for i in range(2, 1001) if is_prime(i)]

for b in primes_under_1000:
    # We check both positive and negative b (though b must be prime, 
    # the problem mentions |b| <= 1000).
    for b_val in [b, -b]:
        for a in range(-999, 1000):
            count = count_consecutive_primes(a, b_val)
            if count > max_primes:
                max_primes = count
                best_a = a
                best_b = b_val

print(f"Maximum primes: {max_primes}")
print(f"Coefficient a: {best_a}, b: {best_b}")
print(f"Product (a * b): {best_a * best_b}")