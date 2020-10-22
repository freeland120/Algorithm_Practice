#Outer triangle sum


ans = []

while True:
    n = int(input())
    total1 = 0
    arr = []

    if n == 0:
        break
    
    for i in range(n):
        data = list(map(int,input().split()))
        arr.append(data)

    for i in range(n):
        if i == 0 or i == 1 or i == n-1:
            total1 += sum(arr[i])
        else:
            total1 += (arr[i][0]+arr[i][-1])

    ans.append(total1)


for i in range(len(ans)):
    print("Case #%d:%d" %(i+1,ans[i]))
