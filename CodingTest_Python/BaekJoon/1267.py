
n = int(input())

Times = list(map(int,input().split()))

Y = 0
M = 0

for i in Times:

    Y = Y + i // 30 * 10 + 10 # 영식 요금제
    M = M + i // 60 * 15 + 15 # 민식 요금제


if Y > M:
    print("M",M)
elif Y < M:
    print("Y",Y)
else:
    print("Y M",Y)