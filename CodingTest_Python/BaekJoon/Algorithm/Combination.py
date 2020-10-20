#n자리 k진수 기본형을 이용해서 중복을 허용하지 않는 "조합(Combination)"만들기


def recur(depth,start):
    if depth == k:
        for i in range(k):
            print(arr[i], end=" ")
        print()
        return

    

    for i in range(start,n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        arr.append(i)
        recur(depth+1,i+1)
        arr.pop()
        visited[i] = False



n,k = map(int,input().split())
arr = []
visited = [False]*(n+1)

recur(0,1)


# #1~n까지 k개를 뽑을때 "중복허용"한 조합(Combination) 만들기
# def recur(depth,start):
#     if depth == k:
#         for i in range(k):
#             print(arr[i],end=" ")
#         print()
#         return


#     for i in range(start,n+1):
        
#         arr.append(i)
#         recur(depth+1,i)
#         arr.pop()
        

# n, k = map(int,input().split())

# arr = []

# recur(0,1)








#기본적인 조합코드(start를 이용했지만 2차원 재귀를 하기에는 한계가 있는 코드)

# def recur(depth,start):
    
#     if depth == n:
#         for i in range(n):
#             print(arr[i], end=" ")
#         print()
#         return

    
#     for i in range(start,k):
#         arr.append(i)
#         recur(depth+1,i+1)
#         arr.pop()




# n, k = map(int,input().split())



# arr = []

# recur(0,0)



#4번째 공식(현재껄 고른다 안고른다.)
#조합코드 2번째 경우
# def recur(cur):
#     if cur == n:
#         return

#     arr.append(cur)
#     recur(cur+1)
#     arr.pop()
#     recur(cur+1)





# n = 4
# arr =[]

# recur(0)






# def recur(cur,cnt):

#     if cnt > k:
#         return

#     if cur == n:
#         print(arr)
#         return

    

#     arr.append(cur)
#     recur(cur+1,cnt+1)
#     arr.pop()
#     recur(cur+1,cnt)






# n = 4 
# k = 2

# arr = []
# recur(0,0)




# def recur(cur,cnt):

#     if cnt > k:       # 더 많이 고른걸 컷팅하는것이고
#         return

#     if cur == n:
#         if cnt <= 1: # 여기는 더 적게 고른걸 가지치기하는것이라고 생각하면 됨
#             return
#         print(arr)
#         return

    

#     arr.append(cur)
#     recur(cur+1,cnt+1)
#     arr.pop()
#     recur(cur+1,cnt)






# n = 4 
# k = 2

# arr = []
# recur(0,0)




#4개 공식에 대해서 트리구조 설명하기


