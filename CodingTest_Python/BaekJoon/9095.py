answer = 0

def recur(depth,goal):
    global answer

    if depth == goal:
        answer += 1
        return

    elif depth > goal:
        return

    recur(depth+1,goal)
    recur(depth+2,goal)
    recur(depth+3,goal)    

    return


T = int(input())
arr = []
while True:
    if T == 0:
        break

    k = int(input())

    recur(0,k)

    arr.append(answer)

    answer = 0
    
    T -= 1

for i in arr:
    print(i)