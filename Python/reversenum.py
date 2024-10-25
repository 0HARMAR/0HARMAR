numlist = [1,2,3,4,5] # reversenum list

n = 0

for num in numlist:
    for next in numlist[numlist.index(num)::]:
        if next < num:
            n+=1

print(n)