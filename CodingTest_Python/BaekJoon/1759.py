
from itertools import combinations
from itertools import permutations

L, C = map(int,input().split())

Word_List = set(input().split())


A = set(['a','e','i','o','u'])
B = set(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'])


Word_List_A = Word_List & A




sorted_list = sorted(Word_List)


result = combinations(sorted_list,L)


for i in result:
    num = len(set(i) & Word_List_A)

    if num == 0 or (L-num) < 2:
        continue
    
    print(''.join(i))
