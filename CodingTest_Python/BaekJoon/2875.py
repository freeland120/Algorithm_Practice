



N,M,K = map(int,input().split())

cnt = 0

while N >= 0 and M >=0 and N+M >= K:
    N -= 2
    M -= 1
    cnt +=1

print(cnt-1)

