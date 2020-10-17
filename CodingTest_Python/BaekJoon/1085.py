x, y, w, h = map(int,input().split())

arr = [x,y,w-x,h-y]

result = min(arr)

print(result)





#x, y, w, h = map(int,input().split())
# if abs(x-w) >= abs(y-h):
#     print(abs(y-h))
# else:
#     print(abs(x-w))