#Problem 44
pentnum=[]
for i in range(1,3000):
    b=(3*i)-1
    a=i*b//2
    pentnum.append(a)
pair=[]
for i in range(len(pentnum)):
    for j in range(i+1,len(pentnum)):
        a=pentnum[i]
        b=pentnum[j]
        if a+b in pentnum and abs(a-b) in pentnum:
            pair.append(a)
            pair.append(b)
print(pair)
print(abs(pair[0]-pair[1]))