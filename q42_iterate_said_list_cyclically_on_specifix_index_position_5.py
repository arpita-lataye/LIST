v=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
k=5
m=[]
for i in range(len(v)):
    m.append(v[k%(len(v))])
    k+=1
print(m)


# ''' Iterate the said list cyclically on specific index position 5 :
#  ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']'''
