a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
b=20
c=30
count=0
inner=1
m=[]
while i<len(a):
    if count==2:
        if inner==1:
            m.append(b)
            inner+=1
        elif inner==2:
            m.append(c)
            inner=1
        count=0
    m.append(a[i])
    count+=1
    i+=1
print(m)
           