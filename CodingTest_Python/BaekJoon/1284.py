#Default 1.양쪽 경계선 여백2cm(고정) => +2
    # 2. 숫자 사이 간격 3자리면 2cm, 4자리면 3cm => len(Input) -1
    # 3. 0이면 4cm, 1이면 2cm, 이외 숫자는 3cm

result = []


while True:
    Input = input()
    if Input == "0":
        break

    
    size = [4,2,3,3,3,3,3,3,3,3]
    
    total = len(Input)+1
    for i in Input:
        total += size[int(i)]
        if i == "0":
            total += 4
        elif i == "1":
            total += 2
        else:
            total += 3
    result.append(total)
    

for i in result:
    print(i)