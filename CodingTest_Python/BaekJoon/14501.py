# 퇴사




# solve(i)=현재i일 일때, 백준이가 얻을 수 있는 최대수익

# solve(i) = max( solve(i + T[i]) + P[i], solve(i+1) )





def solve(depth):
    if depth > n:
        return
    
    result = 0

    if (depth+Time[depth] <= n+1):
        result = solve(depth + Time[depth] + Pay[depth])
    
    return  max(result,solve(depth+1))

    




n = int(input())

Time =[]
Pay = []


for i in range(1,n+1):
    T,P = map(int,input().split())
    Time.append(T)
    Pay.append(P)


print(Time)
print(Pay)


solve(1)