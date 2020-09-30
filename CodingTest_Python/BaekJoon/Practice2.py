

import math



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
            print(i,"는 소수입니다.")
    return count


N = int(input())

result = isPrime(N)

if result == True:
    print(N,"은 소수입니다❗❗❗")

else:
    print(N,"은 소수가 아닙니다❗❗❗")


result2 = countPrimes(N)

print(N,"까지의 소수의 갯수는:",result2,"개 입니다.")
