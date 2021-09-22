a=[]
size=int(input('enter size of the list:'))
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
minval=min(a)
print('minimum number from the list:',minval)