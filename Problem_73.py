#Problem 73
import math
from fractions import Fraction
def proper_reduced(a1):
    if math.gcd(a1.numerator,a1.denominator)==1:
            return True
    else:
        return False
l=set()
count=0
for i in range(1,1000):
    for j in range(1,1000):
        a1=Fraction(i,j)
        if proper_reduced(a1):
            l.add(a1)
#print(len(l))
l2=sorted(l)
#print(l2)
new1=set()
for i in l2:
    if i>Fraction(1, 3) and i<Fraction(1,2):
        count=count+1
#print(new1)
print(count)