arr = list(map(int, input().split()))
arr.sort()
if arr[1] - arr[0] == arr[2] - arr[1]:
    print(arr[2] * 2 - arr[1])
elif arr[1] - arr[0] > arr[2] - arr[1]:
    print(arr[1] * 2 - arr[2])
else:
    print(arr[1] * 2 - arr[0])