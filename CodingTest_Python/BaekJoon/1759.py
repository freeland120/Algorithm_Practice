
# from itertools import combinations
# from itertools import permutations

# L, C = map(int,input().split())

# Word_List = set(input().split())


# A = set(['a','e','i','o','u'])
# B = set(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'])


# Word_List_A = Word_List & A




# sorted_list = sorted(Word_List)


# result = combinations(sorted_list,L)


# for i in result:
#     num = len(set(i) & Word_List_A)

#     if num == 0 or (L-num) < 2:
#         continue
    
#     print(''.join(i))




# k가 문자열의 갯수
# n은 문자열의 길이


def check(cur):
    #최소 1개 이상의 모음과 2개 이상의 자음이 있으면 출력
        aeiou = 0
        for i in range(n):
            if(cur[i] == 'a' or cur[i] == 'e' or cur[i] == 'i' or cur[i] == 'o' or cur[i] == 'u'):
                aeiou +=1
        if aeiou >=1 and n - aeiou >= 2:
            return True
        else:
            return False


def recur(cur,start):

    if len(cur) == n:
        if(check(cur)):
            print(cur)
        return

    for i in range(start,k):
        recur(cur + arr[i],i+1)
        

n, k = map(int,input().split())

arr = []
