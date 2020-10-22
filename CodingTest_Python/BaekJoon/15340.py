#Sim Card


arr = [[30,40],[35,40],[40,20]]

ans = []

while True:

    c,d = map(int,input().split())
    total1 = 0
    total2 = 0
    total3 = 0

    if c == 0 and d == 0:
        break
    else: 
        total1=c*arr[0][0] + d*arr[0][1]
        total2=c*arr[1][0] + d*arr[1][1]
        total3=c*arr[2][0] + d*arr[2][1]

    result = min(total1,total2,total3)

    ans.append(result)

for i in ans:
    print(i)