

import math
import time


def isPrime(N):
    for i in range(2,math.floor(math.sqrt(N))+1):
        if N % i == 0:
            return False

    return True


def countPrimes(N):
    count = 0 

    for i in range(2,N+1):
        if isPrime(i):
            count += 1
            
    return count



def countPrimes2(N):
    sieve = [False,False] + [True] * (N-1)
    primes = []
    count2 = 0
    for i in range(2,N+1):
        primes.append(i)
    
        for j in range(i * 2, N+1, i):
            sieve[j] = False

    #print(sieve)

    for k in range(2,N+1):
        if sieve[k]:
            count2 += 1       

    return count2



N = int(input())

# result = isPrime(N)

# if result == True:
#     print(N,"은 소수입니다❗❗❗")

# else:
#     print(N,"은 소수가 아닙니다❗❗❗")


countPrimes_time_start = time.time()
result2 = countPrimes(N)
countPrimes_elapsed = time.time() - countPrimes_time_start
print(N,"까지의 소수의 갯수는:",result2,"개 입니다.")
print(countPrimes_elapsed, '초')
print(countPrimes_elapsed/60, '분')
print(countPrimes_elapsed/60/60, '시간')



countPrimes2_time_start = time.time()
result3 = countPrimes2(N)
countPrimes2_elapsed = time.time() - countPrimes2_time_start
print(N,"까지의 소수는:",result3,"개 입니다.")
print(countPrimes2_elapsed, '초')
print(countPrimes2_elapsed/60, '분')
print(countPrimes2_elapsed/60/60, '시간')




