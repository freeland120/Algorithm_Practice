arr = []

for i in range(n):
    a,b = map(int,input().split())  
    x = 1
    for i in range(b):
        x = x*a
        x = x%10
    arr.append(x)
    

print(arr)
for i in arr:
    if i == 0:
        print(10)
    else:
        print(i)




n = int(input())

arr = []

for _ in range(n):
    a,b = map(int,input().split())  

    arr.append( ((a % 10) ** b) % 10)  

for i in arr:
    if i == 0:
        print(10)
    else:
        print(i)


n = int(input())







#1009번(분산처리)
#이 문제 같은 경우, 범위가 넒고 큰 데이터들 중에서 원하는 데이터를 찾기위해 반복된 부분을 걸러냄으로서 문제해결의 시간복잡도를 줄일 수 있다.
#1~9까지의 수 중에서 1,5,6을 '밑수'로 가진다면 '지수'가 무엇이 오든지 1,5,6이 나오기 때문에 '밑수'를 출력해주면 된다.
#같은 방식으로 4,9를 '밑수'로 가진다면 '지수'가 2로 나누어 떨어지면 항상 일의 자리는 6이 나오고, 그렇지 않다면 '밑수' 4,9를 출력해주면 된다.
#같은 방식으로 2,3,7,8을 '밑수'로 가진다면 '지수'가 4로 나누어 떨어진다면 항상 일의 자리는 6이 나온다.


n = int(input())

arr1 = []
arr2 = []

for _ in range(n):
    a,b = map(int,input().split())
    arr1.append(a)
    arr2.append(b)



for i in range(n):
    base = arr1[i] % 10


    if base == 0:
        print(10)
    
    elif base in [1,5,6]:
        print(base)

    elif base in [4,9]:
        if arr2[i] % 2 == 0:
            print( base ** 2 % 10 )
        else:
            print(base)

    elif base in [2,3,7,8]:
        if arr2[i] % 4 == 0:
            print( base ** 4 % 10)
        else:
            print( base ** (arr2[i] % 4) % 10)
         

