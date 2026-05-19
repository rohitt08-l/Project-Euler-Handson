#Problem 49
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
c=0
for i in range(1000,10000):
    if is_prime(i):
        for j in range(i+1,10000):
            if is_prime(j):
                k=j+(j-i)
                if k<10000 and is_prime(k):
                    if sorted(str(i))==sorted(str(j))==sorted(str(k)):
                        print(str(i)+str(j)+str(k))