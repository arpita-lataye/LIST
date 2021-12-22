# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']

v=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
k=3
m=[]
for i in range(len(v)):
    m.append(v[k%(len(v))])
    k+=1
print(m)