import sys


n = int(sys.stdin.readline())

Sum = 0

for i in range(n):
    
    Sum += int(sys.stdin.readline())

result = Sum - (n-1)      #멀티탭의 플러그 개수를 다 더한 후에  '멀티탭 개수 -1'을 빼준다!!!! 그러면 총 플러그 개수가 됨
print(result)