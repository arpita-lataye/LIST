a=[]
size=int(input('enter size of the list:'))
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
a.sort()
print('min value:',a[0])
print('second min value:',a[1])