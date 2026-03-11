#Problem 7
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n=1
count=0
while count< 10001:
    n=n+1
    if is_prime(n):
        count=count+1
    
print(n)