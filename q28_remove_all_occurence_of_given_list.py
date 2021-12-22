a=[1,1,2,3,4,5,1,2]
m=[]
for i in range(len(a)):
    if a[i] != 1:
        m.append(a[i])
print(m)