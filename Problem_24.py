#Problem 24
from datetime import datetime,date
t1=datetime.now()
import itertools
my_list = [0,1,2,3,4,5,6,7,8,9]
perms = itertools.permutations(my_list)
a=[]
# Convert the iterator to a list and print the results
for p in perms:
    #my_list = list(map(int, str(p))
    num = int("".join(map(str, p)))
    a.append(num)
print(a[999999])
t2=datetime.now()
print(t2-t1)