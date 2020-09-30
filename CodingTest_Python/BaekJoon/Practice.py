
# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)

# arr = []
# visited = []
# cnt = 0

# n = 0

# def recur(cur):
#     cnt = 0
#     if cur == n:
#         cnt += 1
#         return

#     for i in range(n):
#         if visited[i]:
#             continue
    
#         visited[i] = True
#         arr.append(i)
#         recur(cur+1)
#         arr.pop()
#         visited[i] = False




# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)
# #n-Rook
# arr = []
# visited = []
# cnt = 0

# n = 0

# def recur(cur):
#     cnt = 0
#     if cur == n:
#         cnt += 1
#         return

#     for i in range(n):
#         if visited[i]:
#             continue
    
#         visited[i] = True
#         arr.append(i)
#         recur(cur+1)
#         arr.pop()
#         visited[i] = False


# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)
# #n-Queen

# def recur():
#     #가지치기(정답이 안될것 같으면 return을 해라 ,정답인지 아닌지 판단하는 부분이 가지치기라고 생각하면 된다.)
#     #기저
#     #재귀

# arr = []
# n = 0

# def recur(cur):
#     for i in range(cur-1):
#         if cur-1 - i == abs(arr[i] - arr[cur-1]):
#             return

#         if cur == n:
#             cnt += 1
#             return
#         for i in range(n):
#             if visited[i]:
#                 continue

#             visited[i] = True
#             arr.append(i)
#             recur(cur+1)
#             arr.pop()
#             visited[i] = False



#질문하는 방식
#1.내가 이런 로직으로 이런 시도를 했다(기대값)
#2.이렇게 잘 못 나오더라(경향,어떻게 잘 못 나오는지)
#3.이런게 틀린 것 같아서 시도를 해봤는데 결과가 어떻게 달라지더라(디버깅)

#로직
#경향
#비버깅