#n자리 k진수를 이용해서 중복을 허용하지 않는 기본형 "순열(Permutation)"만들기



#두 번째 공식
def recur(depth):
    if depth == k:
        for i in range(k):
            print(arr[i],end=" ")
        print()
        return
    

    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = True
        arr.append(i)
        recur(depth+1)
        arr.pop()
        visited[i] = False


n,k = map(int,input().split())
arr = []
visited = [False]*(n+1)

recur(0)


#1~n까지 k개를 뽑을때 "중복허용"한 순열(permutation) 만들기

# def recur(depth):
#     if depth == k:
#         for i in range(k):
#             print(arr[i],end=" ")
#         print()
#         return

#     for i in range(1,n+1):
#         #if visited[i]:
#             #continue

#         #visited[i] = True
#         arr.append(i)
#         recur(depth+1)
#         arr.pop()
#         #visited[i] = False
        


# n, k = map(int,input().split())

# arr = []

# #visited = [False]*(n+1)

# recur(0)


# n자리 m진수 순열 뽑아내기
# def recur(depth):
#     if depth == n:
#         print(arr)
#         return
    


#     for i in range(1,n+1):
#         if visited[i]:
#             continue
        
#         visited[i]=True
#         arr.append(i)
#         recur(depth+1)
#         arr.pop()
#         visited[i]=False




# n,m = map(int,input().split())
# arr = []
# visited = [False]*(n+1)


# recur(0)