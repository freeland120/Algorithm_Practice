

import sys


arr = []

ans = []

for i in range(0,32):
    arr.append(2 ** i)


n = int(sys.stdin.readline())

for _ in range(n):
    target = int(sys.stdin.readline())
    if target in arr:
        ans.append(1)       
    else:   
        ans.append(0)

for i in ans:
    print(i)