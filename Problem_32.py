#Problem 32
def is_pandigital(a, b, c):
    s = str(a) + str(b) + str(c)
    return len(s) == 9 and set(s) == set("123456789")


products = set()

# Case 1: 1-digit × 4-digit
for a in range(1, 10):
    for b in range(1000, 10000):
        c = a * b
        if is_pandigital(a, b, c):
            products.add(c)

# Case 2: 2-digit × 3-digit
for a in range(10, 100):
    for b in range(100, 1000):
        c = a * b
        if is_pandigital(a, b, c):
            products.add(c)

print(sum(products))