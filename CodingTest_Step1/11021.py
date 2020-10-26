import sys

T = int(input())

arr = []

for _ in range(T):
    a = map(int,sys.stdin.readline().split())
    arr.append(sum(a))

for i in range(1,len(arr)+1):
    print("Case #%d: %d" %(i,arr[i-1]))