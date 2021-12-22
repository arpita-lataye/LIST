
z=['1', '2', '3', '4', '5', '6', '7', '8']
x=[]
i=0
while i<(len(z)-1):
    # n=z[i],z[i+1]
    # print(n)
    x.append(z[i]+z[i+1])
    z.remove(z[i])
    i+=1
print(x)