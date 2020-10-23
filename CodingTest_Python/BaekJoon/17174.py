#전체 계산 횟수


n,m = map(int,input().split())


ans = n
tmp = n


while True:
    if tmp < m:
        break

    ans += (tmp//m)
    tmp //= m

print(ans)