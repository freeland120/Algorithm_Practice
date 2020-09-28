
import math


def Amazing_Prime(num):
    for i in range(2, math.floor(math.sqrt(int(num)))+1):
        if int(num) % i == 0:
            return
    
    if len(num) == n:
        print(num)
        return

    for j in prime:
        Amazing_Prime(num+j)



n = int(input())

start = ['2','3','5','7']
prime = ['1','3','7','9']

for s in start:  
    Amazing_Prime(s)






# 2023 신기한 소수

#일단 소수란 1과 자기자신으로밖에 나누어 지지 않는 수를 말한다.
#소수 판별법
# 1.N이 1이면 소수가 아니다.
# 2.2부터 N-1 까지의 자연수들로 순서대로 N을 나눠서 나누어 떨어지는 수가 하나도 없으면 N은 소수이다.
# 에라토스테네스의 체를 이용하거나 python의 slice문법을 활용하면 쉽게 풀 수 있음