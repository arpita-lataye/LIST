
a=[34.67, 12, -94.89, 'Python', 0, 'C#']
m=[]
for i in range(len(a)):
    # print(a[i])
    if type(a[i]) is int:
        m.append(a[i])
print(m)