
#주사위


s1,s2,s3 = map(int,input().split())


arr = [0] *(s1+s2+s3+1)


for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            arr[i+j+k] += 1



tmp = 0
index = 0

for i in range(s1+s2+s3+1):
    if tmp == arr[i]:
        continue
    
    elif tmp < arr[i]:
        tmp = arr[i]
        index = i

print(index)