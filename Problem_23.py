#Problem 23
#Funtion that checks if number isabundant
def is_abundant(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i!=n:
                divs.append(i)
            if i != n//i and n//i != n:
                divs.append(n//i)
    #print(sum(divs)-n)
    if sum(divs)>n:
        return True
l1=[] #Finds all abundant num and add to ist
for i in range(28124):
    if is_abundant(i):
        l1.append(i)
limit=28123
l2=set()  #Store num that can be written as sum of 2 abundant num
for i in range(len(l1)):#checks all pairs of abundant num
    for j in range(len(l1)):
        a1=l1[i]+l1[j]
        if a1<=limit:
            l2.add(a1)
total=0
for i in range(1,limit+1):
    if i not in l2:#if number cannot written as sum of 2 abunant num
        total=total+i
print(total)