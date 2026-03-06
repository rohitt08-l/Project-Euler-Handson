#Problem 0
sum=0
for x in range(144000):
    a=x*x
    if a%2==1:
        sum=sum+a
    else:
        continue
print(sum)