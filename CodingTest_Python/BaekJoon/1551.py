#수열의 변화

import sys
import copy

n,k = map(int,input().split())

data = list(map(int,input().split(",")))



while k:
    tmp = []
    for i in range(1,len(data)):
        tmp.append(data[i]-data[i-1])

    data = copy.deepcopy(tmp)

    k -= 1

print(','.join(map(str,data)))