#Problem 39
max_count=0
best_p=0
for p in range(1,1000):
    count=0
    for j in range(1,p//3):#Because 2 side cant never be 3x
        for k in range(j+1,p//2):#Because 2 side cant never be 2x
    
            i = (j*j + k*k) ** 0.5
    
            if i.is_integer() and i+j+k == p:
                count=count+1
    if count>max_count:
        max_count=count
        best_p=p
print(best_p)