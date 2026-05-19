#Problem 29
l=[]
for i in range(2,101):
    for j in range(2,101):
        a=i**j
        if a not in l:
            l.append(a)
l.sort()
print(len(l))