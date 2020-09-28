

from itertools import combinations_with_replacement


N, M = map(int,input().split())


data = list(map(int,input().split()))

data.sort()

CWR = combinations_with_replacement(data,M)


for i in CWR:
    print(' '.join(map(str,i)))

























#N과 M (8)