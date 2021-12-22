li=["red","yellow","maroon"]
s=[]
for i in range(len(li)):
    l=[]
    for j in range(len(li[i])):
        l.append(li[i][j])
    s.append(l)
print(s)