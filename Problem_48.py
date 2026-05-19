#Problem 48
sum=0
for x in range(1,1001):
    a=x**x
    #print(a)
    sum=sum+a
#print("Total",sum)
print("Last 10 digits",str(sum)[-10:])