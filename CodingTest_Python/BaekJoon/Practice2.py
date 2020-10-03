

# import math
# import time


# def isPrime(N):
#     for i in range(2,math.floor(math.sqrt(N))+1):
#         if N % i == 0:
#             return False

#     return True


# def countPrimes(N):
#     count = 0 

#     for i in range(2,N+1):
#         if isPrime(i):
#             count += 1
            
#     return count



# def countPrimes2(N):
#     sieve = [False,False] + [True] * (N-1)
#     primes = []
#     count2 = 0
#     for i in range(2,N+1):
#         primes.append(i)
    
#         for j in range(i * 2, N+1, i):
#             sieve[j] = False

#     #print(sieve)

#     for k in range(2,N+1):
#         if sieve[k]:
#             count2 += 1       

#     return count2



# N = int(input())

# # result = isPrime(N)

# # if result == True:
# #     print(N,"은 소수입니다❗❗❗")

# # else:
# #     print(N,"은 소수가 아닙니다❗❗❗")


# countPrimes_time_start = time.time()
# result2 = countPrimes(N)
# countPrimes_elapsed = time.time() - countPrimes_time_start
# print(N,"까지의 소수의 갯수는:",result2,"개 입니다.")
# print(countPrimes_elapsed, '초')
# print(countPrimes_elapsed/60, '분')
# print(countPrimes_elapsed/60/60, '시간')



# countPrimes2_time_start = time.time()
# result3 = countPrimes2(N)
# countPrimes2_elapsed = time.time() - countPrimes2_time_start
# print(N,"까지의 소수는:",result3,"개 입니다.")
# print(countPrimes2_elapsed, '초')
# print(countPrimes2_elapsed/60, '분')
# print(countPrimes2_elapsed/60/60, '시간')


# from itertools import combinations

# N,M = map(int,input().split())

# data = []

# for i in range(1,N+1):
#     data.append(i)

# result = combinations(data,M)

# print('\n'.join(map(str,result)))




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
        if col[i] == col[k] or abs(col[i]-col[k]) == (i - k):
            flag = False
        k += 1
    return flag



N = int(input())

col = [0]*(N+1)

n_queens(0,col)





