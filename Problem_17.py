#Problem 17
from num2words import num2words
sum=0
for i in range(1,1001):
    a=num2words(i).replace(" ","")
    a=a.replace("-","")
    sum=sum+len(a)
print(sum)