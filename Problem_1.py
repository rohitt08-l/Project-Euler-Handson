#problem 1 
x=1
a=0
b=0
for x in range (924000):
    #print(x)
    if x%2==1:
        b=(x*x)+b
print(b)