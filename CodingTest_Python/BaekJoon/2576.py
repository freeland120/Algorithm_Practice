

arr = []
sum = 0

for _ in range(7):
    x = int(input())
    if x%2 != 0:
        arr.append(x)
        sum += x
    else:
        continue
    
if arr:
    print(sum)
    print(min(arr))
else:
    print(-1)