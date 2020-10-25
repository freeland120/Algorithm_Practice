


#완전탐색 컨셉 생각!, 브루트 포스 방법

n = int(input())


x = 1
y = 1


for i in range(1,n):

    if x == 1:
        x = y + 1
        y = 1
        

    else:
        x -= 1
        y += 1
print(x,y)
