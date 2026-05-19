#Problem 35
prime=set()
def is_prime(n):
    if n<1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    else :
        prime.add(n)
        return True
for i in range(2,1000000):
    if is_prime(i)==True:
        prime.add(i)
cir_prime=set()
def circullar_prime(n):
    s = str(n)
    rotations =set()
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if int(rotated) not in prime:
            return False
        
    return True
for i in range(2,1000000):
    if circullar_prime(i)==True:
        cir_prime.add(i)
print(cir_prime)
print(len(cir_prime))