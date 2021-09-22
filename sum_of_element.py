a=[]
size=int(input("enter size of the list:"))
for i in range(size):
    val=int(input("enter number:"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print('sum of lis element:',sum)