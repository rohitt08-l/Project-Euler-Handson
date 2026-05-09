#problem 1 
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9 the sum is 23. The sum of these multiples of 3 or 5 below 1000 is."""
x=1
a=0
b=0
for x in range (1000):
    if x%3==0 or x%5==0:
        b=x+b
print("The sum of the multiples of 3 or 5 below 1000 is",b)