import math

import time



def isPrime(n):

  for i in range(2,math.floor(math.sqrt(n))+1):

​    if n % i == 0:

​      return False

  return True





def countPrimes(n):

  count = 0

  for i in range(2,n+1):

​    if isPrime(i):

​      count += 1

​      print(i,"는 소수입니다.")

  return count





N = int(input())



start = time.time()





M = countPrimes(N)



elapsed = time.time() - start





print(N,"이하에는", M, "개의 소수가 있습니다.")

print(elapsed, '초')

print(elapsed / 60, '분')

print(elapsed/60/60, '시간')






def countPrimes2(N):



  sieve = [False,False] + [True]*(N-1)



  *#primes = []*

  count = 0



  for i in range(2,N+1):

​    if sieve[i]:

​      *#primes.append(i)*

​      count += 1

​    for j in range(i*2, N+1, i):

​      sieve[j] = False

  

  return count



Num = int(input())



print(countPrimes2(Num))