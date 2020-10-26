import sys
N,X = map(int,input().split())

arr = list(map(int,sys.stdin.readline().split()))

for i in arr:
    if X > i:
        print(i,end=" ")
    else:
        continue



