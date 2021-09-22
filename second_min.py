a=[]
size=int(input('enter size of the list:'))
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
minval=min(a)
print('min value in the list is:',minval)
a.remove(minval)
secmin=min(a)
print('second min value in the list is:',secmin)