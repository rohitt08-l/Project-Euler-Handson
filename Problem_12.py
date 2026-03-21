#Problem 12
newl1=[1]
d=1
for i in range(2,50000):
    d=d+i
    newl1.append(d)
    a=i+1
def divisors(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n//i:
                divs.append(n//i)
        
    return len(divs)
gd=[]
for i in newl1:
    if divisors(i) >=500:
        gd.append(i)
    else:
        continue
print(gd[0])