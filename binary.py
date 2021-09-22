# a=[1,0,0,1,1,0,1,1]
# i=0
# j=0
# sum=0
# while i<len(a):
#     d=a[-i]
#     sum=sum+(2**j)*d
#     j=j+1
#     i=i+1
# print(sum)

binary_number=[1,0,0,1,1,0,1,1]
i=0
length=len(binary_number)
a=[]
while i<length:
    length=length-1
    a.append(binary_number[length])
print(a)
j=0
sum=0
length=len(a)
while j<length:
    n=2**j*a[j]
    sum=sum+n
    j=j+1
print(sum)
print(a[j])




print()
print(2**2*2)