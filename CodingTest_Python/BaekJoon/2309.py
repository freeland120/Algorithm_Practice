#일곱 난쟁이

#그냥 무식한 방법...
#9명 중 두 명을 빼서 100이 된다면 그 원소들을 리스트에서 빼주고 정렬 후 출력!

arr = []


for i in range(9):
    arr.append(int(input()))

total = sum(arr)

one = 0
two = 0

for i in range(8):
    for j in range(i+1,9):
        if total - (arr[i]+arr[j]) == 100:
            one = arr[i]
            two = arr[j]

arr.remove(one)
arr.remove(two)

arr.sort()

for i in arr:
    print(i)