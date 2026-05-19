#Problem 73 
#This is also correct but it works slow
# import math
# from fractions import Fraction
# count=0
# for i in range(1,12001):
#     for j in range(1,12001):
#         a1=Fraction(i,j)
#         if math.gcd(a1.numerator,a1.denominator)==1 and a1>Fraction(1, 3) and a1<Fraction(1,2):
#             count=count+1
# print(count)
import math
count = 0
for d in range(1,12001):
    start = d//3 + 1 # smallest integer greater than d/3
    end = (d-1)//2 # largest integer smaller than d/2
    for n in range(start, end+1):
        # check if fraction is reduced
        if math.gcd(n,d) == 1:
            count += 1
print(count)