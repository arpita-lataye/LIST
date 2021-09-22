numbers=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(numbers):
    num=numbers[i]
    if num>=20 and num<40:
        print(numbers[i])
        count = count+1
    i=i+1
print(count)