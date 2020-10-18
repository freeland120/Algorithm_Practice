a,b = map(int,input().split())


max_num = max(a,b)
min_num = min(a,b)

x = max_num - min_num

s = (x * (x+1)) // 2

print(s + (min_num*(x+1)))