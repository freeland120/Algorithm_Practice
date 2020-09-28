from itertools import product

N, M = map(int,input().split())

data = list(map(int,input().split()))

data.sort()


PRO = product(data,repeat=M)


for i in PRO:
    print(' '.join(map(str,i)))




# N과 M (7)
# 이 문제는 자연수 N,M이 주어졌을때 1부터 N까지 자연수 중에서 M개를 뽑는다.
# 이 때, 1~N의 범위안에 있는 모든 숫자를 가지고 하는것이 아니라 N개의 수가 입력받도록한다. 
# 입력받은걸 중복을 허용하고 "사전 순으로 증가"시킨다.
# 나는 product 파이썬 표준 라이브러리를 사용해 풀었다.

# 데이터 type이 int형인 N,M을 입력받는다.
# 입력받은 값을 data리스트에 넣었으면 sort()함수를 통해 오름차순 정렬해준다.
# data리스트에서 1개를 뽑아 나열(순열은 순서가 상관이 있다.)
# product를 시키면 tuple값으로 담김
#여기서 핵심은 tuple값으로 담긴걸 str형태로 뽑아서 출력해야함
# i를 뽑아낼 때 tuple => str로 map메서드를 사용
# join메서드를 사용하는 이유는 리스트의 요소를 공백기준으로 연결해 문자열로 만들기 위함