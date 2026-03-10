#problem 6
"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
#sum
x=1
sum=0
for x in range(101):
    sum=sum+x
sum_square=sum*sum
print('Square of sum =',sum_square)

square=0
for x in range(101):
    square=square+(x*x)
print(' sum  of square =',square)
diff=sum_square - square
print("Diffence =",diff)