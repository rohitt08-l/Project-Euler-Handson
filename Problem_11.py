digits = 13
max_product = 0
print(len(num))
 
for i in range(len(num) - digits + 1):
    product = 1
    for j in range(digits):
        product *= int(num[i + j])
    if product > max_product:
        max_product = product
 
print(max_product)