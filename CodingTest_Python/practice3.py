

## <문제> 거스름돈
# n = 1260

# count = 0


# array = [500,100,50,10]



# for i in array:
#     result = n // i
#     count += result
#     n %= i

# print(count)


## <문제> 1이 될 때까지

# N, k = map(int,input().split())


# result = 0

# while True:

#     target = (N//k) * k
#     result += (N - target)
#     N = target

#     if N < k :
#         break

#     result += 1
#     N //= k

# result += (N-1)
# print(result)


## 내가 푼 방식
# N, k = map(int,input().split())

# count = 0

# while True:
#     if N % k == 0:
#         count += 1
#         N //= k
#         continue

#     elif N < k:
#         break
#     else:
#         N -= 1
#         count += 1

# print(count)


## <문제> 곱하기 혹은 더하기

# data = str(input())

# result = int(data[0])


# for i in range(1,len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)


##동,남,서,북

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]


# x = 0
# y = 0

# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     print(nx,ny)


# for i in range(5):
#     for j in range(5):
#         print('(',i,',',j,')',end = " ")
#     print()






from itertools import permutations

N, M = map(int, input().split())


data = []

for i in range(1,N+1):
    data.append(i)


P = list(permutations(map(str,data), M))  # iter(tuple)

print(P)

for i in P:
    print(' '.join(map(str, i)))  # tuple -> str







