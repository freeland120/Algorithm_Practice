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

# n = int(input())

# print(~n)


##1060~62(비트 연산자 부분으로 안품)


##1063
# a, b = list(map(int,input().split()))


# print(a if a>b else b) 


##1064

# a, b, c = list(map(int,input().split()))

# result = min(a,b,c)

# print(result)

##1065
# a, b, c = list(map(int,input().split()))

# for i in a,b,c :

#     if i % 2 == 0:
#         print(i)
    
##1066
# a , b, c = list(map(int,input().split()))

# for i in a,b,c:
#     if i % 2 ==0:
#         print("even")
#     else:
#         print("odd")


##1067

# a = int(input())

# if a > 0:
#     print("plus")
#     if a % 2 == 0:
        
#         print("even")
#     else:
#         print("odd")
# elif a < 0:
#     print("minus")
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")


##1068

# n = int(input())

# if n >= 90:
#     print("A")
# elif n >= 70:
#     print("B") 
# elif n >= 40:
#     print("C") 
# else:
#     print("D")


##1069
# a = input()

# if a == 'A':
#     print("best!!!")
# elif a == 'B':
#     print("good!!") 
# elif a == 'C':
#     print("run!") 
# elif a == 'D':
#     print("slowly~")
# else:
#     print("what?")



# x = input()

# def switch(x):
#     result = {'A':'best!!!', 'B':'good!!!', 'C':'run!', 'D':'slowly~'}.get(x,'what?')
#     return result

# print(switch(x))





##1070
# n = int(input())

# if n == 12 or n == 1 or n == 2:
#     print("winter")
# elif n == 3 or n == 4 or n == 5:
#     print("spring")
# elif n == 6 or n == 7 or n == 8:
#     print("summer")
# elif n == 9 or n == 10 or n == 11:
#     print("fall")



##1071

# n = list(map(int,input().split()))


# for i in n :
#     if i != 0:
#         print(i)
#     else:
#         break

##1072
# N = input()

# n = list(map(int,input().split()))

# for i in n :
#     print(i)

##1073

# n = list(map(int,input().split()))

# for i in n:
#     if i != 0:
#         print(i)
#     else:
#         break

##1074

# n = int(input())

# while n >= 1:
#     print(n)

#     n -= 1


##1075

# n = int(input())

# while n >= 0:
#     if n == 0 :
#         break
#     else:
#         print(n-1)
#         n -= 1


##1076


# a = ord(input())
# b = ord('a')


# while a >= b:
#     print(chr(b), end = " ")
#     b += 1


##1077


# n = int(input())

# n2 = int(0)


# while n >= n2 :
#     print(n2)
#     n2 += 1


# n = int(input())


# for i in range(n+1):
#     print(i)


##1078

# n = int(input())

# sum = 0

# for i in range(1,n+1):
#     if( i % 2 == 0):
#         sum += i
#         #print(sum + "+" + i + "=")
#     else:
#         continue

# print(sum)



##1079
# char = list(map(str,input().split()))

# for i in char:
#     if i == 'q':
#         print(i)
#         break
#     else:
#         print(i)


##1080

# n = int(input())

# sum = 0

# for i in range(1,n):
#     sum += i
    
#     if sum >= n:
#         print(i)
#         break

    

##1081
# n, m = list(map(int,input().split()))

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i,j)



##1082

# a = int(input(),16)

# b = hex(a)[2].upper()


# for i in range(1,16):
#     c = hex(i)[2:].upper()
#     d = hex(a*i)[2:].upper()
    
#     print(b + "*" + c + "=" + d)
