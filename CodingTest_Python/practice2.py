
#from bisect
#from itertools
#from heapq
#from collections
#from math


# n = 1260
# count = 0

# array = [500,100,50,10]

# for coin in array:
#     count += n //coin

#     n %= coin

# print("거스름듬돈을 최소로 만드는 갯수는:",count)


# #그리디 탐색이라는 것은 지금 상태에서 전체 상황을 고려하지 않고 가장 좋아보이는 걸 계속 고르는 탐색 방법



# # N,K를 공백을 기준으로 구분하여 입력 받기
# n , k = map(int,input().split())


# result = 0


# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
#     target = (n//k) * k
#     result += (n - target)
#     n = target
#     # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)



# data = input()

# for i in range(len(data)):
#     print(data[i])




#먼저 02987을 입력받는다고 하자


# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])


# for i in range(1,len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])

#     if num <=1 or result <=1 :
#         result += num
#     else:
#         result *= num

# print(result)



# 구현(implementation)

# for i in range(5):
#     for j in range(5):
#         print('(',i,',',j,')', end=' ')
#     print()


# # 동, 북 ,서 ,남
# dx = [0,-1,0,1]
# dy = [1,0,-1,0]

# #현재 위치
# x, y = 2, 2


# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     print(nx, ny)


# list1 = list(map(int,input().split()))


# print(list1)



#하루는 24시간 일주일 168시간 
#24시간 * 60 분 = 1440분
#하루 86,400초 




# h = int(input())


# count = 0 


# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1

# print(count)


n = int(input())


for i in range(1,n+1):
    for j in range(1,n+1):
        print('(',i,',',j,')',end = '')
    print()







