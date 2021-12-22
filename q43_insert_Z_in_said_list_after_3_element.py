x=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
i=0
j='Z'
count=0
inner=1
b=[]
while i<len(x):
    if count==2:
        if inner==1:
            b.append(j)
            inner+=1
        elif inner==2:
            b.append(j)
            inner=1
        count=0
    b.append(x[i])
    count+=1
    i+=1
print(b)