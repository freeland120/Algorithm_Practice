


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