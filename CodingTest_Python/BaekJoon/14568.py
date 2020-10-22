

#2017 연세대학교 프로그래밍 경시대회
#"조합"

import sys

n = int(sys.stdin.readline())
r = 0

for i in range(2, n-1,2):
    r = r + (n-i-2)//2

print(r)
