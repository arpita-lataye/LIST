z=[4,5,5,5,3,8]
for i in range(len(z)-2):
    if z[i]==z[i+1] and z[i+1]==z[i+2]:
        print(z[i])

input=[1, 1, 1, 64, 23, 64, 22, 22, 22]
for i in range(len(input)-2):
    if input[i]==input[i+1] and input[i+1]==input[i+2]:
        print(input[i])