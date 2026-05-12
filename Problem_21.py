num=[]
def divisors(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n//i:
                divs.append(n//i)
    
    return sum(divs)-n

def isamical(i,j):
    if divisors(i)==j and divisors(j)==i:
        # num.append(i)
        # num.append(j)
        num.extend([i,j])
for i in range(10000):
    for j in range(i):
        isamical(i,j)
print(num)
print(sum(num))