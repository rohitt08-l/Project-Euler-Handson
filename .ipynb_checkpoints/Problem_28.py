#Problem 28
n=100
sum=0
mult=1
for x in range(1,n+1):
    mult=x*mult
print(mult)
list_mult=list(map(int,str(mult)))
print(list_mult)
# sum_values=sum(list_mult)
# print(sum_values)
sum1=0
for x in list_mult:
    sum1=sum1+x
print(sum1)