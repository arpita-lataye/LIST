l=[[1,2,4],[2,4,4],[1,2]]
s=[]
u=0
q=0
r=0
for i in range(len(l)):
    for j in range(len(l[i])):
        if j==0:
           u=u+l[i][j] 
        if j==1:
           q=q+l[i][j] 
        if j==2:
           r=r+l[i][j]
s.append(u)
s.append(q)
s.append(r)
print(s) 