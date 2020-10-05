#n자리 k진수 만드는 방법 공식 외워!!!!



def recur(depth):
    if depth == n:
        for i in arr:
            print(i,end=" ")
        print()
        return
    
    for i in range(1,k):
        arr.append(i)
        recur(depth+1)
        arr.pop()




arr =[]
n,k = map(int,input().split())


recur(0)