# 세 막대
#  c가 가장 긴 변의 길이라고 한다면, c < a+b 가 성립해야 삼각형을 만들 수 있다.
arr = list(map(int,input().split()))


arr.sort()


while True:
    if arr[2] < arr[1] + arr[0]:
        total = arr[2] + arr[1] + arr[0]
        print(total)
        break
    else:
        arr[2] -= 1
    

