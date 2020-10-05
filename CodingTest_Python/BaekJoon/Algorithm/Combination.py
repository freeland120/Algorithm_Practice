#n자리 k진수 기본형을 이용해서 중복을 허용하지 않는 "조합(Combination)"만들기


def recur(depth,start):
    if depth == k:
        for i in range(k):
            print(arr[i], end=" ")
        print()
        return

    

    for i in range(start,n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        arr.append(i)
        recur(depth+1,i+1)
        arr.pop()
        visited[i] = False



n,k = map(int,input().split())
arr = []
visited = [False]*(n+1)

recur(0,1)


#1~n까지 k개를 뽑을때 "중복허용"한 조합(Combination) 만들기
def recur(depth,start):
    if depth == k:
        for i in range(k):
            print(arr[i],end=" ")
        print()
        return


    for i in range(start,n+1):
        
        arr.append(i)
        recur(depth+1,i)
        arr.pop()
        

n, k = map(int,input().split())

arr = []

recur(0,1)








