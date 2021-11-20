a="The Robert Hook Is A Scientist"
b=[]
c=[]
count=0
count1=0
for i in a:
    if i>="A" and i<="Z":
        b.append(i)
        count=count+1
    if i>="a" and i<="z":
        c.append(i)
        count1=count1+1
print(b,"count=",count)
print(c,"count=",count1)