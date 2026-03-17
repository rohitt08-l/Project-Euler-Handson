#Problem 10
"""Find the sum of all the primes below two million."""
def prime_sum(b):
    total = 0
    
    for i in range(2, b+1):
        is_prime = True
        
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime:
            total += i
            
    return total

print(prime_sum(2000000))