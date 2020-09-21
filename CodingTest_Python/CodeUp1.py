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
