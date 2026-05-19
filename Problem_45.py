#Problem 45
#1.Triangle
triangle=[]               
for i in range(1,100000):
    b=i+1
    a=i*b//2
    triangle.append(a)
#2. Pentagonal
pentnum=set()
for i in range(1,100000):
    b=(3*i)-1
    a=i*b//2
    pentnum.add(a)

#3Hexagonal
hexagonal=set()
for i in range(1,100000):
    b=(2*i)-1
    a=i*b
    hexagonal.add(a)
for i in triangle:
    if i in pentnum and i in hexagonal:
        print(i)   
# print(triangle) 
# print(pentnum)   
# print(hexagonal)
    