
m=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
n=[]
k=[]
count=0
for i in range(len(m)):
    if count==5:
        n.append(k)
        k=[]
        count=1
    else:
        count+=1
    k.append(m[i])
n.append(k)
print(n)