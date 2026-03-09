#Problem 5
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
"""
import math
def lcm(a,b):
    c=a*b // math.gcd(a,b)
    return c
result=1
for i in range(1,21):
    result=lcm(result,i)
print(result)