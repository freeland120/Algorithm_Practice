




# arr = []


# arr.append(list(map(int,input().split())))

# print(arr[0][0]+arr[0][-1])


arr = []

while True:
    n = int(input())
    
    
    if n == 0:
        break

    for i in range(1,n+1):
        data = list(map(int,input().split()))
        arr.append(data)

    total = 0
    for i in range(n):
        if len(arr[i]) == 1 or len(arr[i]) == n:
            total += arr[i][i]




# total = 0

# for i in range(n):
#     if i == 0:
#         total += arr[0][0]
#     elif i == n-1:
#         for i in arr:
#             total += i
#     else:
#         total += arr[i][0] + arr[i][-1]


# print(total)