a=[]
size=int(input('enter the size of the list:'))
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
min=a[0]
for i in range(size):
    if a[i]<min:
        min=a[i]
print('min number',min)