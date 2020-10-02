
lis = [22,11,6,3,88,99]

for i in range(len(lis)):
    for j in range(i,len(lis)):
        if lis[i] > lis[j]:
            temp = lis[i]
            lis[i] = lis[j]
            lis[j] = temp

print(lis)