from itertools import combinations


N, M = map(int,input().split())


data = []


for i in range(1,N+1):
    data.append(i)


C = combinations(data,M)


for i in C:
    print(' '.join(map(str,i)))


# N과 M (2)
# 이 문제는 자연수 N,M이 주어졌을때 1부터 N까지 자연수 중에서 
# "중복 없이" M개를 고르고 고른 수열은 "오름차순"이여야하는 문제
# 나는 combinations 파이썬 표준 라이브러리를 사용해 풀었다.
# 데이터 type이 int형인 N,M을 입력받는다.
# 1~N까지 수를 담아둘 리스트 선언
# 1~N까지 자연수를 담는다.
# data리스트에서 1개를 뽑아 나열(순열은 순서가 상관이 있다.)
# combinations을 시키면 tuple값으로 담김
#여기서 핵심은 tuple값으로 담긴걸 str형태로 뽑아서 출력해야함
# i를 뽑아낼 때 tuple => str로 map메서드를 사용
# join메서드를 사용하는 이유는 리스트의 요소를 공백기준으로 연결해 문자열로 만들기 위함