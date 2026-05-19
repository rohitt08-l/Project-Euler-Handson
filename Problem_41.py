# Problem 41

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True


def pandigital(n):
    digits = set(map(int, str(n)))
    l = len(str(n))
    p = set(range(1, l+1))
    if digits == p:
        return True
    else:
        return False


n = 7654321   # start from largest possible 7-digit pandigital

while n > 1:
    if isprime(n) == True and pandigital(n) == True:
        print(n)
        break
    n = n - 1