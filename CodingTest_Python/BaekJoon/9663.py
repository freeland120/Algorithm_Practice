


# arr = []
# visited = []

# #n자리 k진수 중복없이 만든는 방법(한 케이스내,중복없는 순열)
# n = 0
# def recur(cur):
#     if cur == n:
#         return

#     for i in range(n):
#         if visited[i]:
#             continue
    
#         visited[i] = True
#         arr.append(i)
#         recur(cur+1)
#         arr.pop()
#         visited[i] = False




# def n_queens(i,col): 
#     n = len(col) - 1

#     if promising(i,col):
#         if (i == n):
#             print(col[1:n+1])
#         else:
#             for j in range(1,n+1):
#                 col[i+1] = j
#                 n_queens(i+1, col)



# def promising(i,col):
#     k = 1
#     flag = True
#     while (k < i and flag):
#         if(col[i] == col[k] or abs(col[i]-col[k]) == (i-k)):
#             flag = False
#         k += 1
#     return flag


# n = 4

# col = [0] * (n+1)
# print(col)
# n_queens(0,col)



# 1. n_queens함수는 i값과 col배열을 받는데 여기서 i는 depth이다.
# 2.n=len(col) -1 왜냐하면 0부터 시작하니까(루트노드의 depth가 0부터 시작하니까)
# 3.if promising(i,col): i번째 depth의 컬럼을 가지고 얘가 프라미싱한지 봐야겠지
# 4.if i==n: 만약 i의 depth가 n과 같다면!(여기서 n은 n-queen) 그리고 같다는 말은 내가 끝까지 왔다는 의미











def n_queens(i,col):
    n = len(col) - 1

    if promising(i,col):
        if i == n:
            print(col[1:n+1])
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queens(i+1,col)

def promising(i,col):
    k = 1
    flag = True

    while(k<i and flag):
        if ( col[i]==col[k] or abs(col[i]-col[k]) == (i - k)):
            flag = False
        k += 1
    return flag    




n = int(input())


col = [0] * (n+1)


n_queens(0,col)








def n_queens(i,col):
    n = len(col) - 1
    
    if promising(i,col):
        
        if i == n:
            print(col[1:n+1])
            
            
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queens(i+1,col)
                
    


def promising(i,col):
    k = 1
    flag = True
   
    while k<i and flag:
        if (col[i]==col[k] or abs( col[i]-col[k] == (i-k) )):
            flag = False
        k += 1
    
    return flag 


n = int(input())

col = [0] * (n+1)

n_queens(0,col)








