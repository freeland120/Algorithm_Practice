




#1단계 : 5
#2단계 : 5+7 = 12
#3단계 : 5 + 7 + 10 = 22
#4단계 : 5 + 7 + 10 + 13 = 35
#5단계 : 5 + 7 + 10 + 13 + 16 = 51


n = int(input())


first = 5
increase = 7


for i in range(1,n):
    first += increase
    increase += 3

print(first % 45678)