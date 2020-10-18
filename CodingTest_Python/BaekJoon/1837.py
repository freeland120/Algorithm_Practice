
import sys

p,k = map(int,sys.stdin.readline().split())

arr = [0] * (10000001)

result = 0

for i in range(2,1001):
    if arr[i] == 0:
        num = i * 2

        while num < 1000001:
            arr[num] = 1
            num += i

for i in range(2,1000001):
    if arr[i] == 0:
        if p % i == 0:
            result = i
            break

if result == 0:
    print("GOOD")
else:
    if result < k:
        print("BAD",result)
    else:
        print("GOOD")

