



N,L,D = map(int,input().split())

arr = []


for i in range(N):
    for j in range(L):
        arr.append(1)
    
    for j in range(5):
        arr.append(0)
    

bell = 0

while True:
    if bell >= len(arr):
        break

    elif arr[bell] == 0:
        break

    else:
        bell += D


print(bell)