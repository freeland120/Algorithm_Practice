
def recur(depth):
    if depth == n:
        print(arr)
        for i in arr:
            print(i,end=" ")

        print()
        return

    
    for i in range(k):
        arr.append(i)
        recur(depth+1)
        arr.pop()



n,k = map(int,input().split())


arr = []

recur(0)
