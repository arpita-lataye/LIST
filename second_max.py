a=[]
size=int(input('enter size of the list:'))
for i in range(size):
    val=int(input('enter number:'))
    a.append(val)
maxval=max(a)
print('max value in the list is:',maxval)
a.remove(maxval)
secmax=max(a)
print('second max value in the list:',secmax)