a=[1,3,5,7,9,11,15,19]
i=0
b=[]
while i<len(a)-1:
    c=a[i+1]
    c=c-a[i]
    b.append(c)
    i=i+1
print(b)


# a=[4,2,6,8,7,2,5]
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i+1]
#     c=c-a[i]
#     b.append(c)
#     i=i+1
# print(b)