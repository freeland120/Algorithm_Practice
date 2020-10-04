
#재귀함수에서는 "종료조건"을 명시하는게 중요하다.

# #기본형
# def recursive_function(depth):

#     if depth == 100:
#         return
    
#     print(depth,'번째 재귀함수가',depth+1,'번째 재귀함수를 호출합니다.')
#     recursive_function(depth+1)
#     print(depth,'번째 재귀함수가 종료됩니다')




# recursive_function(1)





#팩토리얼 구현 예제

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