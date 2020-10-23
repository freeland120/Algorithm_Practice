#피드백

n = int(input())
arr = [0 for _ in range(n)]
arr[0] = 1
arr[1] = 2
arr[-1] = 997

for i in range(1,n):
    if arr[i] == 0 :
        arr[i] = arr[i-1] +1
    
print(n)
print(*arr)