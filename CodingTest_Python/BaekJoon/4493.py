



n = int(input())

for _ in range(n):
    arr = [0,0]

    m = int(input())
    for _ in range(m):
        a,b = input().split()

        if a == "R" and b == "P":
            arr[1] += 1
        elif a == "R" and b == "S":
            arr[0] += 1
        elif a == "P" and b == "R":
            arr[0] += 1
        elif a == "P" and b == "S":
            arr[1] += 1
        elif a == "S" and b == "P":
            arr[0] += 1
        elif a == "S" and b == "R":
            arr[1] += 1
    
    if arr[0] > arr[1]:
        print("Player 1")
    elif arr[0] == arr[1]:
        print("TIE")
    else:
        print("Player 2")