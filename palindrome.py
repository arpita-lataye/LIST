name=['n','i','t','i','n']
i=0
length=len(name)
a=[]
while i<length:
    length=length-1
    a.append(name[length])
print(a)
if a==name:
    print("it is a polindrome ")
else:
    print("it is not a polindrome")