


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
# CALL 010-4169-5319d
# CALL 010-4769-5319
# CALL 010-4869-5319
# SMS 010-4969-5319
# CALL 010-4069-5319




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