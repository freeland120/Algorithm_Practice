




N = int(input()) #참가자 수


prize_list = []  #상금을 비교하는 리스트


for i in range(N):
    a,b,c = map(int,input().split())     #N명이 주사위 3개 던져서 만드는 값들

    #모두 같은 경우
    if a == b == c:
        prize = 10000 + 1000*a
    
    #2개만 같은 경우
    elif a == b != c:
        prize = 1000 + 100*a
    elif b == c != a:
        prize = 1000 + 100*b
    elif c == a != b:
        prize = 1000 + 100*c
    
    #모두 각기 다른 상금이였을 경우
    else:
        max_num = max([a,b,c])
        prize = max_num * 100
    
    prize_list.append(prize)

print(max(prize_list))
