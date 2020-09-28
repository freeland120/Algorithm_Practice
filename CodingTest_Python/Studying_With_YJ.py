


# def add_play(genre, idx, plays):
#     genre[0] += plays[idx]
    
#     if genre[1] == -1 or plays[genre[1]] < plays[idx]:
#         genre[2] = genre[1]
#         genre[1] = idx
#     elif genre[2] == -1 or plays[genre[2]] < plays[idx]:
#         genre[2] = idx

# def solution(genres, plays):
#     answer = []
#     genre = {}
    
#     for i in range(len(genres)):
#         genre[genres[i]] = [0, -1, -1]
    
#     for i in range(len(genres)):
#         add_play(genre[genres[i]], i, plays)
        
#     result = sorted(genre.values(), key=lambda x:x[0], reverse=True)
    
#     for i in result:
#         if i[1] != -1:
#             answer.append(i[1])
#         if i[2] != -1:
#             answer.append(i[2])
    
#     return answer






#     from collections import deque

# def solution(prices):
#     answer = []
#     stack = deque()
    
#     prices[-1] = -1
    
#     for i in range(len(prices)):
#         answer.append(0)
    
#     for i in range(len(prices)):
#         while len(stack) != 0 and prices[stack[-1]] > prices[i]:
#             answer[stack[-1]] = i - stack[-1]
#             stack.pop()
#         stack.append(i)
    
#     return answer


#     armygo
# 1q2w3e4r!!
# 1q2w3e4r!!



# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean



n = int(input()) # 송수신 기록의 수  
logs = [ input().strip() for i in range(n) ]  # 송수신 기록

ans = 1
answer = [logs[0]]
count = [1]
for i in range(1, n):
	if answer[-1] == logs[i]:
		count[-1] += 1
	else:
		ans += 1
		answer.append(logs[i])
		count.append(1)
		
print(ans)
for i in range(ans):
	print(answer[i], end=" ")
	if(count[i] > 1):
		print("(",count[i],")")
	else:
		print("")

# 10
# CALL 010-4169-5319
# SMS 010-4269-5319
# SMS 010-4369-5319
# CALL 010-4569-5319
# CALL 010-4269-5319
# CALL 010-4169-5319
# CALL 010-4769-5319
# CALL 010-4869-5319
# SMS 010-4969-5319
# CALL 010-4069-5319




# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


uid = input().strip()
pw1 = input().strip()
pw2 = input().strip()
ans = True

if len(uid) < 3 or len(uid) > 20:
	ans = False

for i in uid:
	if not((i >= '0' and i <= '9') or (i >= 'a' and i <= 'z')):
		ans = False
		
if len(pw1) < 8 or len(pw1) > 20:
	ans = False

alpha = 0
number = 0
mark = 0

for i in pw1:
	if i >= '0' and i <= '9':
		number += 1
	elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
		alpha += 1
	else:
		mark += 1
		
if number == 0 or alpha == 0 or mark == 0:
	ans = False
	
if pw1 != pw2:
	ans = False

if ans:
	print("pass")
else:
	print("fail")










# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
user_input2 = list(map(int,input().split()))

count = []

for i in range(1010):
	count.append(0)
	
for i in user_input2:
	count[i] += 1
	
answer = []

while len(answer) != user_input:
	for i in range(1, 1001):
		if count[i] > 0:
			count[i] -= 1
			answer.append(i)
	
ans = 0
for i in range(1, user_input):
	if answer[i] > answer[i-1]:
		ans += 1
		
print(ans)

#print ("Hello Goorm! Your input is " + user_input)










# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
@description
        로봇 방문 순서에 따라 배열 m을 채워주는 함수

@param m    로봇 방문 순서를 저장할 r행 c열의 배열, m[i][j] := (i행 j열)칸의 로봇의 방문 순서 번호
@param r    행의 수 
@param c    열의 수 
"""
def simulate(m, r, c):
    #begin of function
		
		dx = [0, 1, 0, -1]
		dy = [1, 0, -1, 0]
		
		x = 0
		y = 0
		direction = 0
		number = 1
		
		while number <= r*c:
			m[x][y] = number
			number += 1
			
			nx = x + dx[direction]
			ny = y + dy[direction]
			
			if nx < 0 or nx >= r or ny < 0 or ny >= c or m[nx][ny] != 0:
				direction = (direction + 1) % 4
				
			x += dx[direction]
			y += dy[direction]
    
    #end of function


"""
메인 함수에는 테스트케이스와 입출력에 대한 기본적인 뼈대 코드가 작성되어 있습니다. 
상단의 함수만 완성하여도 문제를 해결할 수 있으며, 
메인 함수를 제거한 후 스스로 코드를 모두 작성하여도 무방합니다.
단, 스스로 작성한 코드로 인해 발생한 에러 등은 모두 참가자에게 책임이 있습니다.
"""
if __name__ == "__main__":
    #테스트케이스의 수를 입력받는다 
    case_num = int(input())

    #각 테스트케이스에 대해 순서대로 데이터를 입력받고 정답을 출력한다 
    for case_index in range(1, case_num+1):

        #행과 열의 수를 입력받는다 
        r, c = [ int(e) for e in input().split() ]

        # 0으로 초기화 된 r행 c열의 리스트를 생성한다 
        m = [ [0] * c for row_index in range(r) ] 

        #주어진 함수를 실행하여 각 칸을 로봇 청소기가 방문하는 순서를 리스트에 저장한다
        simulate(m, r, c)

        #케이스 번호를 출력한다 
        print('Case #%d' % case_index)

        #각 칸의 방문 순서를 출력 형식에 맞게 출력한다
        for i in range(r):
            print(*m[i], sep=' ')