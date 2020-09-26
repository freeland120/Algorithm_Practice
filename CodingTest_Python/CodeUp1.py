# #기초100문제

# #1001
# print("Hello")

# #1002
# print("Hello World")

# #1003
# print("Hello\nWorld")

# #1004
# print("\'Hello\'")

# #1005
# print("\"Hello World\"")

# #1006
# print("\"!@#$%^&*()\"")

# #1007
# print("\"C:\\Download\\hello.cpp\"")

# #1008
# print("\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518")

# #1010
# n = int(input())

# print(n)

# #1011
# char = str(input())
# print(char)

# char2 = input()
# print(char2)

# #1012
# n = float(input())
# print(format(n,".6f"))

# #1013
# a, b = map(int,input().split())
# print(a,b)

# #1014
# a, b = map(str,input().split())
# print(b,a)

# #1015
# n = float(input())
# print(format(round(n,3),".2f"))   

# round(n,3)
# result2 = format(n,".2f")
# print(result2)

# #1017
# n = int(input())
# for i in range(3):
#     print(n,end=' ')

# #1018
# hour, minute = input().split(':')
# print(hour + ":" + minute)


##1019

# from datetime import datetime

# year, month, day = input().split(".")

# print("%04d" %int(year), end ='.')
# print("%02d" %int(month), end='.')
# print("%02d" %int(day))

# from datetime import datetime

# year, month, day = input().split(".")

# Year=year.zfill(4)
# Month=month.zfill(2)
# Day=day.zfill(2)

# print(Year+"."+Month+"."+Day)

##1020
# a = "5000"

# print(a.zfill(5))     //zfill(width) 함수 사용
# print(a.rjust(5,"a"))     //rjust(width, [fillchar]) 함수 사용

# Birthday, etc = input().split("-")

# print(Birthday + etc)


##1021
# Char = str(input())

# print(Char)


##1022
# String = str(input())

# print(String)


##1023
# int_number, float_number = input().split(".")

# print(int_number)
# print(float_number)

##1024
# word = list(str(input()))

# for i in word:
#     print("'"+i + "'")

##1025

# n = input()

# print("[%d]" %(int(n[0])*10000))
# print("[%d]" %(int(n[1])*1000))
# print("[%d]" %(int(n[2])*100))
# print("[%d]" %(int(n[3])*10))
# print("[%d]" %(int(n[4])))


# n2 = list(input())

# tmp = 10000

# for i in range(len(n2)):
#     if tmp != 0 :
#         print("[%d]" %(int(n2[i])*tmp))
#         tmp /= 10


##1026
# hour, minute, second = input().split(":")
# print("%d" %int(minute))

##1027

# year, month, day = input().split(".")

# print("%02d" %int(day), end="-")
# print("%02d" %int(month), end="-")
# print("%d" %int(year))

# year, month, day = input().split(".")


# print(day.zfill(2),month.zfill(2),year.zfill(4),sep="-")

##1028
# n = int(input())

# print(n)

##1029
# n = float(input())

# result= format(n, ".11f")
# print(result)

##1030
# n = input()
# print(n)

##1031
# n = input()

# print("%o" % int(n))

##1032
# n = input()

# print("%x" % int(n))

##1033
# n = input()
# print("%X" % int(n))

##1034

# n = input()

# result = int(n,8)
# print(result)

##1035
# n = input()
# result = int(n,16)
# print("%o" % int(result))


##1036
# char = input()

# print(ord(char))

##1037
# n = int(input())
# result = chr(n)
# print(result)

##1038
# data1, data2 = map(int,input().split())

# print(data1 + data2)


##1039
# data1, data2 = map(int,input().split())

# print(data1 + data2)

##1040
# n = input()
# print("%d" % -int(n))


##1041
# n = input()

# tmp = ord(n) + 1

# result = chr(tmp)

# print(result)

##1042

# a, b = list(map(int,input().split()))

# result = a//b

# print(result)

# x, y = input().split()

# x = int(x)
# y = int(y)

# result2 = x // y
# print(result)

##1043
# a, b = list(map(int,input().split()))

# result = a % b

# print(result)

##1044
# n = int(input())

# n += 1

# print(n)


##1045
# a, b = list(map(int,input().split()))

# data_sum = a + b
# data_sub = a - b
# data_mul = a * b
# data_div = a // b
# data_rest = a % b
# data_div2 = a / b

# result = format(round(data_div2,2),".2f")

# print(data_sum)
# print(data_sub)
# print(data_mul)
# print(data_div)
# print(data_rest)
# print(result)


##1046

# a, b, c = list(map(int,input().split()))

# data_sum = a + b + c
# data_avg = (a+b+c)/3

# result = format(round(data_avg,1),".1f")

# print(data_sum)
# print(result)


##1047

# n = int(input())

# result = (n << 1) # 2로하면 4배 3으로하면 8배 2의 거듭제곱만큼 증가  '>>'는 반대

# print(result)


##1048

# a, b = list(map(int,input().split()))

# result1 = a << b

# print(result1)

##1049
# a, b = list(map(int,input().split()))

# result1 = int(a > b) 

# print(result1)

##1050
# a, b = list(map(int,input().split()))

# result = int(a==b)

# print(result)

##1051
# a, b = list(map(int,input().split()))

# result = int(b >= a)

# print(result)

##1052
# a, b = list(map(int,input().split()))

# result = int(a != b)

# print(result)


##1053
# n = int(input())
# result = int(n != 1)
# print(result)

# n = int(input())

# result = int(bool(not n))

# print(result)


##1054
# a, b = list(map(int,input().split()))

# A = bool(a)
# B = bool(b)

# result = int(A & B)

# print(result)


##1055
# a, b = list(map(int,input().split()))

# A = bool(a)
# B = bool(b)

# result = int(A | B)

# print(result)


##1056
# a, b = list(map(int,input().split()))

# A = bool(a)
# B = bool(b)

# result = int(A^B)

# print(result)


##1057
# a, b = list(map(int,input().split()))

# A = bool(a)
# B = bool(b)

# result = int(A == B)
# result2 = not A^B
# print(result)
# print(result2)


##1058
# a, b = list(map(int,input().split()))

# A = bool(a)
# B = bool(b)

# result = int(not(A|B))

# print(result)


# a, b = list(map(int,input().split()))

# pay = 0

# def price_mul(price,a):
#     pay = price * a
#     return pay
# print("지급할 금액:", price_mul(a,b))




##1059

n = int(input())

print(~n)


