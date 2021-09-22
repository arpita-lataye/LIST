a=[]
size=int(input('enter size of the list:'))
for i in range(size):
    val=int(input('enter the number:'))
    a.append(val)
a.sort()
print('max number:',a[size-1])
print('second max number:',a[size-2])