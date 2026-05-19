#Problem 37
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


l1 = []

for i in range(10,1000000):

    b = str(i)
    trunctable= True

    # check left truncations
    for j in range(len(b)):
        if not is_prime(int(b[j:])):
            trunctable = False
            break

    # check right truncations
    for j in range(len(b)):
        if not is_prime(int(b[:len(b)-j])):
            trunctable = False
            break

    if trunctable:
        l1.append(i)

print(l1)
print(len(l1))
print(sum(l1))