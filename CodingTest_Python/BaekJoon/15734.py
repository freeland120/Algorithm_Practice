
# 양발잡이를 모두 왼발로 취급, 오른발로 취급, 균등하게 분배 했을 때
# 나오는 선수 인원 수 중 최소값을 기준으로 두배를 시켜준다.
L,R,A = map(int,input().split())

while A:
    if L < R:
        L += 1
    else:
        R += 1
    A -= 1

x = abs(L-R)

print(L+R-x)