


N = int(input())

Cup = [1,2,3]


for _ in range(N):
    x, y = map(int,input().split())


    xi = Cup.index(x)
    yi = Cup.index(y)
    

    Cup[xi], Cup[yi] = Cup[yi],Cup[xi]

print(Cup[0])
