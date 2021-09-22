c=[4,9,35,64,86,89,100,121,454,144,265,625]
for i in c:
    j=1
    while j<i:
        if j**j==i:
            print(i,"is a perfect square")
            break
        # else:
        #     print(i,"is not a perfect square")
        # j=j+1
        i=i+1