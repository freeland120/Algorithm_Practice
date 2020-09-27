# data = dict()

# data['사과'] = "Apple"
# data['바나나'] = "Banana"


# print(data['사과'])


# a = dict()

# a['유덕경'] = "Handsome"
# a['유도경'] = "SoSo"

# print(a)

# print(list(a.keys()))
# print(list(a.values()))


# data = set([1,2,3,4,5])
# print(data)

# data2 = {1,2,3,4,5}
# print(data2)


# data2.add(7)
# print(data2)
# print(1 in data2)



# test1 = {'H','e','l','l','o'}

# print(test1)

# test2 = set(['H','e','l','l','o'])
# print(test2)



# #a, b, c, d, e = map(int,input().split())

# #print(a,b,c,d,e)


# #list1 = list(map(int,input().split()))

# #print(list1)



# #n = int(input())
# #m = int(input())


# #arr = []

# #arr.append(list(map(int, input().split())))

# #import sys

# #data = sys.stdin.readline().rstip()

# #print(data)

# print(8, end=' ')
# print(10)



# print(1, end=' ')
# print(2, end=' ')
# print(3, end=' ')
# print(4, end=' ')
# print(5, end=' ')
# print(6, end=' ')
# print(7)


# a = 7

# print("정답은:" + str(a))

# x = 9

# if x >= 10:
#   print(x)
#   print("출력완료")

# print("조건문 끝!")


# My_Score = 97

# if My_Score >= 90:
#   print("당신의 성적은 '수'입니다.")
# elif My_Score >= 80:
#   print("당신의 성적은 '우'입니다.")
# elif My_Score >= 70:
#   print("당신의 성적은 '미'입니다.")
# elif My_Score >= 60:
#   print("당신의 성적은 '양'입니다.")
# else:
#   print("공부를 다시 하셔야 할 것 같아요..")



# a = 97

# if x >=0 and x <= 100:
#   print("x는 0이상 100이하의 수 입니다.")
# else:
#   print("지정된 범위 밖의 수 입니다.")


# for i in range(1,100, 3):
#   print(i)




# array = [('유덕경',27),('유도경',27),('장준영',25),('김형조',27),('장준하',40)]


# result = sorted(array, key=lambda x:x[0])


# print(result)




# from itertools import permutations

# from itertools import combinations

# data = ['유덕경','유도경','김형조','이주영']


# result = list(combinations(data,3))

# print(result)







# from itertools import permutations

# data = ['A','B','C','D']

# result = list(permutations(data))
# result2 = list(combinations(data,2))

# print(result)
# print(result2)




# from itertools import product

# data3 = ['A','B','C']

# result3 = list(product(data,repeat=2))
# print(result3)



# a = dict()

# b = {'유덕경':27, '유도경':27}


# print(b)



# result = list(b.keys())
# result2 = list(b.values())

# print(result)
# print(result2)


# n = int(input())

# data = list(map(int,input().split()))


# data.sort(reverse=True)

# print(n)
# print(data)


# sys.stdin.readline()


# import sys

# data = sys.stdin.readline().rstrip()

# print(data)



# answer = 7

# print(f"정답은 {answer} 입니다.")


# x = 15

# if x > 0 and x < 20:
#   print(x)



# for i in range(2,10):
#   for j in range(1,10):
#     print(i, "X", j, "=", i*j)
#   print()




array = [('유덕경',27), ('유도경',27), ('유래경',29),('누누누',10)]


result = sorted(array,key=lambda x:x[1],reverse=True)


print(result)



list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list3 = list(map(lambda a,b:a+b,list1,list2))

print(list3)


