
#재귀함수에서는 "종료조건"을 명시하는게 중요하다.

# #기본형
# def recursive_function(depth):

#     if depth == 100:
#         return
    
#     print(depth,'번째 재귀함수가',depth+1,'번째 재귀함수를 호출합니다.')
#     recursive_function(depth+1)
#     print(depth,'번째 재귀함수가 종료됩니다')




# recursive_function(1)

# 팩토리얼 구현 예제

# 1.반복적으로 구현한 n!
# def factorial_function1(n):
#     result = 1

#     for i in range(1,n+1):
#         result *= i
#     return result


# N = int(input())
# print(factorial_function1(N))


# 2. 재귀적으로 구현한 n!
# def factorial_function2(n):

#     if n <= 1:
#         return 1
    
#     result = n * factorial_function2(n-1)

#     return result

# N= int(input())
# print(factorial_function2(N))





# def factorial(n):

#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
    
#     result = n * factorial(n-1)
#     return result


def permutation(n,r):

    if n < r:
        return None
    
    numerator = factorial(n)
    dominator = factorial(n-r)

    result2 = numerator//dominator
    return result2


def combination(n,r):

    if n < r:
        return None
    
    numerator = permutation(n,r)
    dominator = factorial(r)

    result3 = numerator // dominator
    return result3

x = int(input())
y,z = map(int,input().split())

# print("입력한 팩토리얼 값은:",factorial(x))
# print("입력한 순열의 값은:",permutation(y,z))
# print("입력한 조합의 값은:",combination(y,z))


answer = 10000000000000000

def recur(cur,cnt,x,y):
    global answer
    if cur == n:

        if cnt == 0:
            return
        answer = min(answer,abs(x-y))
    
        return

    recur(cur+1,cnt+1,x*arr[cur][0],y+arr[cur][1])
    recur(cur+1,cnt,x,y)


n = 4

arr = [[1,7],[2,6],[3,8],[4,9]]



recur(0,0,1,0)

print(answer)


#flood fill 알고리즘