z=[5, 6, [], 3, [], [], 9]
k=[]
for i in range(len(z)):
    # print(z[i])
    if type(z[i]) is not list:
        # z.remove(z[i])
        k.append(z[i])
print(k)
