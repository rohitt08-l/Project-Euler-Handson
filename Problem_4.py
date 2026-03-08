#Problem 4
def is_palindrome(n):
    return str(n) == str(n)[::-1]
a=100
b=1000
largest=0
for i in range(a,b):
    for j in range (a,b):
        product=i*j
        if is_palindrome(product):
            largest=max(largest,product)
print(largest)