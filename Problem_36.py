#Problem 36
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def binary(a):
    b=bin(a)[2:]
    rev=b[::-1]
    if b==rev and b[0]!=0:
        return True
    else:
        return False
sum=0
for i in range(1000000):
    if binary(i)==True and is_palindrome(i)==True:
        sum=sum+i
print(sum)