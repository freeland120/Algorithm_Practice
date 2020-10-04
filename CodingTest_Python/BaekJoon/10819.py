#10819 차이를 최대로

from itertools import permutations


N = int(input())


arr = list(map(int,input().split()))


P = list(permutations(arr))

result = 0

for i in P:
    sums = 0
    for j in range(N-1):
        sums += abs(i[j]-i[j+1])
    result = max(result,sums)

print(result)    
