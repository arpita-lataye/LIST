x=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
y=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
v=[]
for i in range(len(x)):
    v.append(x[i]+y[i])
print(v)