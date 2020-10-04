





def recur(depth):

    if depth == n:
        return

    for i in range(start,k):
        arr.append(i)
        recur(depth+1)
        arr.pop()




n,k = map(int,input().split())

arr = []


recur(n)