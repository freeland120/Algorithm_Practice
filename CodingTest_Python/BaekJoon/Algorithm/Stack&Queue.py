



stack = []


stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop()
stack.append(7)


print(stack[::-1])
print(stack)



from collections import deque


queue = deque()



queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)


print(queue)

queue.popleft()

print(queue)

queue.reverse()
print(queue)