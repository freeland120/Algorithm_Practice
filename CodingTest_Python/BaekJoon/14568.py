

#2017 연세대학교 프로그래밍 경시대회
#"조합"

# import sys

# n = int(sys.stdin.readline())
# r = 0

# for i in range(2, n-1,2):
#     r = r + (n-i-2)//2

# print(r)





n = int(input())
cnt = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (i+j+k) == n and (i >= j+2) and k % 2 == 0:
                cnt += 1

print(cnt)         
    



