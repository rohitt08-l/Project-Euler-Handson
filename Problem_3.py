#Problem 
"""    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""
x=600851475143
l=[]
l2=[]
for i in range (1, int(x**0.5) + 1):
    if x%i==0:
        l.append(i)
    else:
        continue
print(l)
print()
def prime(b):
    for i  in l:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            #print(i)
            l2.append(i)
            
    
a=prime(l)
print(l2)
print(max(l2))