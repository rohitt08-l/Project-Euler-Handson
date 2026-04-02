#Problem 19
from datetime import date, timedelta

start = date(1901,1,1)#start date
end = date(2000,12,31)#end date
days = (end - start).days #range of loop
count=0
for i in range(days+1):
    current = start + timedelta(days=i) #here current is the date 
    if (str(current)[-2::])=="01" and current.weekday()==6: #here we check if date ends with 01 and the weekday is 6 i.e sunday
        #print(current)
        count=count+1
print(count)#print count