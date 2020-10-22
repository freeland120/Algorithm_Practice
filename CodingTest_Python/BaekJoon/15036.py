




def solution(x):
    result = {'0':2,'1':1,'2':1/2,'4':1/4,'8':1/8,'16':1/16}.get(x,10)

    return result


n = int(input())




ans = 0

arr = list(map(str,input().split()))

for i in range(n):
    
    ans += solution(arr[i])

print(ans)



