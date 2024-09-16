import re
handle=open("Actual data.txt")
p=handle.read()
y=re.findall("[0-9]+",p)
sum=0
for x in y:
    p=int(x)
    sum=sum+p
print (sum)
