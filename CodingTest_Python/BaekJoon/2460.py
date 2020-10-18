
#데이터에 1번과 10번일 때 0을 주니깐, 
#내린 사람 수 일때 빼주고 탄 사람 수 일때 더한다.
#그리고 제일 많은 승객 값을 구한다.



x = 0
sum = 0

for i in range(10):
    n,m = map(int,input().split())
    sum -= n
    sum += m

    x = max(x,sum)

print(x)
