#Problem 14
max1=[]
for a in range(1,1000001):
    n=a
    l1=[a]
    
    while n>1:
        if n%2==0:
            n=n//2
            l1.append(n)
        elif n%2==1:
            n=(3*n)+1
            l1.append(n)
    if len(l1)>len(max1):
        max1=l1
#Print the Starting number
print(max1[0])