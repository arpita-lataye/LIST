a=[]
size=int(input('enter size of the list:'))
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
maxval=max(a)
print('maximum number from the list:',maxval)