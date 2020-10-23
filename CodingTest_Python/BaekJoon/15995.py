

#잉여역수 구하기


a, m = map(int,input().split())

arr = []

for i in range(1,1000000):
    if a*i % m == 1:
       arr.append(i)

result = min(arr) 
        
print(result)


    

