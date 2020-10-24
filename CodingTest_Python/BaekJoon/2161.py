
#카드1

n = int(input())


card = [i for i in range(1,n+1)]

x = 0

while card:
    if x % 2:
        card.append(card.pop(0))
    else:
        print(card.pop(0),end=" ")
    
    x += 1