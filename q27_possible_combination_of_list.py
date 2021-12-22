m=[0,9,5]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i!=j and j!=k and i!=k):
                print(m[i],m[j],m[k])