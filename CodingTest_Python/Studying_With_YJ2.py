



3자리 8진수

for i in range(1,8):
    for j in range(8):
        for k in range(8):
            print(i,j,k)





백트래킹을 사용하는 이유 : n중 반복문을 사용하기 위함이다.            

n중 반복문(n입력) k^n



def recur(cur,n,k):
    if cur == n:
        return
    

    for i in range(k):
        print(i, end="")
        
        recur(cur+1,n,k)


recur(0,4,3)







arr = []
visited = []

def recur(cur,n,k):
    if cur == n:
        print(arr)
        return

    
    for i in range(k):
        if visited[i+1]:
            continue

        visited[i+1] = True
        arr.append(i+1)
        recur(cur+1,n,k)
        arr.pop()
        visited[i+1] = False



k, n  = list(map(int,input().split()))

for i in range(k+1):
    visited.append(False)

recur(0,n,k)





기본형
중복제거
오름차순 => 케이스에 중복을 허용하지 않는다.






# 오른차순 기본형

arr = []

def recur(cur,n,k,start):
    if cur == n:
        print(arr)
        return

    
    for i in range(start,k):
        arr.append(i+1)
        recur(cur+1,n,k,i+1)
        arr.pop()



k, n  = list(map(int,input().split()))

recur(0,n,k,0)




3자리 8진수


n, k = map(int,input().split())



for i in range(k):
    for j in range(k):
        for l in range(k):
            print(i,j,l)







