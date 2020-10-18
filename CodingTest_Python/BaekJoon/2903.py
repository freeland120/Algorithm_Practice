#규칙 찾아보기
# 0번 반복 => 점 4개 시작
# 1번 반복 => 점 9개 시작
# 2번 반복 => 점 25개 시작
# +1번 할떄마다 제곱을 하는 규칙



N = int(input())



arr = [4]

x = 2
y = 1

sum = 0

for i in range(1,16):
    x += y
    sum = x ** 2
    arr.append(sum)
    y *= 2

print(arr[N])
