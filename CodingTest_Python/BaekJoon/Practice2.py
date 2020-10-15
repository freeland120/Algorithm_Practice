
# # #1~n까지 k개를 뽑을때 "중복허용"한 조합(Combination) 만들기


# # def recur(depth,start):
# #     if depth == k:
# #         for i in range(k):
# #             print(arr[i],end=" ")
# #         print()
# #         return


# #     for i in range(start,n+1):
        
# #         arr.append(i)
# #         recur(depth+1,i)
# #         arr.pop()
        




# # n, k = map(int,input().split())

# # arr = []

# # recur(0,1)






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





# #n개가 있을 때 나오는 모든 조합을 해보는 코드
# def recur(cur):
#     if cur == n:
#         return

    
#     arr.append(cur)
#     recur(cur+1)
#     arr.pop()
#     recur(cur+1)



# def recur(cur):
#     if cur == n:
#         print(arr)
#         return

    
#     arr.append(cur)
#     recur(cur+1)
#     arr.pop()
#     recur(cur+1)



# arr =[]

# n = 4

# recur(0)










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



def solution(s):
    ans = 0
    num = list(reversed(s))
    num_dic = {}

    for i in range(10):
        num_dic[str(i)] = i

    for i, n in enumerate(num):
        if n == "-":
            ans *= -1
        elif n == "+":
            continue
        else:
            ans += num_dic[n]*(10**i)
    return ans
        

s = input()


print(solution(s))






































