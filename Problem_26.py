#Problem 26
max_len = 0
result = 0

for i in range(2,1000):
    r = 1
    seen = []

    while r not in seen and r != 0: #check if upated remainder is not present in list and remainder not equal to 0
        seen.append(r)
        r = (r * 10) % i

    if len(seen) > max_len:
        max_len = len(seen)
        result = i

print(result)