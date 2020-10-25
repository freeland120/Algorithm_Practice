


import sys


T = int(input())

arr = []

for _ in range(T):
    a = map(int,sys.stdin.readline().split())
    result=sum(a)
    arr.append(result)

for i in arr:
    print(i)



